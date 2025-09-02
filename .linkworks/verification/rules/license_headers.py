import os
import re

from jinja2 import Environment, BaseLoader
from lara.api.document import Document
from lara.logger import logger


LICENSE_HDR_LINES = """This file is part of project link.developers/Student Guide.
It is copyrighted by the contributors recorded in the version control history of the file,
available from its original location https://github.com/tuc-nt-df/student-guide.

SPDX-License-Identifier: MPL-2.0
"""


# matches "##/*// comment text //***#"
# Note: Whitespaces before the closing comment character are required in order to
#       allow for "http://example.com/"
re_comment_content = re.compile("^\\W+\\s*(.*?)(\\s+\\W*)?$")

# .bat files use the REM command for comments ("REM comment"), this might be prefixed with @ to prevent it from being echoed
# Some people (ab)use labels for comments (":: comment")
# Note: (?i) = case insensitive comparison, (?=\s|$) ensures that "REM abc" and "REM\n" work, but "REMcommand a" doesn't
re_comment_content_bat = re.compile("(?i)^(?:@?rem|::)(?=\\s|$)\\s*(.*?)(\\s+\\W*)?$")

re_bat_echo_off = re.compile("(?i)^@?ECHO\\s+OFF")
re_unix_header = re.compile("^#!")


def verify(repository, template):
    errors = list()
    warnings = list()

    logger.debug("Enumerating files ...")
    files = repository.get_files(
        include_patterns=[
            ".*\\.(bat|sh|yaml|yml)$",
            ".*\\.(c|cc|cpp|cxx|h|hh|hpp|hxx|py|fbs)$",
            "CMakeLists.txt$",
        ],
        exclude_patterns=[
            ".lara.yml",
            ".liam.yml",
            ".github/",
            ".linkworks/",
            "linkworks.*",
            "RELICENSE/",
        ])

    logger.debug("Rendering license template ...")
    license_template = Environment(loader=BaseLoader()).from_string(LICENSE_HDR_LINES.strip())
    license_header = license_template.render({**repository.environment}).splitlines(keepends=True)

    for file in files:
        logger.debug("Checking license of {} ...".format(file))
        document = Document()
        document.load_file(file)

        # if the file is empty, then no header is required
        if len(document) == 0:
            return errors, warnings

        # automatically chose the right RegEx based on the file extension
        _, fileext = os.path.splitext(file)
        fileext = fileext.casefold()

        if fileext == ".bat":
            comment_regex = re_comment_content_bat
            header_regex = re_bat_echo_off  # let .bat files begin with "@echo off"
        else:
            comment_regex = re_comment_content
            header_regex = re_unix_header

        searching = True
        tid = 0
        for rid, rline in enumerate(document):
            if tid >= len(license_header):
                break

            rline = rline.strip()
            if len(rline) == 0 and searching:
                continue  # skip empty lines

            # do a special check for file headers (used for scripts on Unix)
            if rid == 0:
                if header_regex.match(rline):
                    continue  # skip the header

            lmatch = comment_regex.match(rline)
            # Note: When there is no match, we compare the full line. (e.g. in C comment blocks, not line every has comment characters)
            if lmatch:
                if len(lmatch.groups()) > 0:
                    rline = lmatch.groups()[0].strip()
                else:
                    rline = ""

            if len(rline) == 0 and searching:
                continue  # skip empty lines that contain only comment characters

            tline = license_header[tid].strip()
            
            if tline != rline:
                print("Lines don't match in {}: '{}' vs '{}'".format(file, tline, rline))
                break

            searching = False
            tid += 1

        if tid < len(license_header):
            # unable to find line of the template
            errors += ["License header mismatch in {}".format(file)]

    return errors, warnings
