#!/usr/bin/env python3
#
# NOTE: This script has been automatically generated.
# Any changes will be lost when the configuration is rerendered!

import sys
import os
import yaml
import subprocess

def getGitCommitCount():
    # git rev-list HEAD --count
    proc = subprocess.Popen(["git", "rev-list", "HEAD", "--count"], stdout=subprocess.PIPE, universal_newlines=True)
    proc.wait()
    if proc.returncode == 0:
        output = proc.stdout.readlines()
        if len(output) > 0:
            return int(output[-1])  # last line = number of commits
    print("Warning: Unable to determine Git commit count! Falling back to BUILD_VERSION = 0!")
    return 0

buildVerInherit = ('BUILD_VERSION' in os.environ)
if not buildVerInherit:
    os.environ['BUILD_VERSION'] = str(getGitCommitCount())
condarcInherit = ('CONDARC' in os.environ)

shortBuildPath = ("GITHUB_ACTIONS" in os.environ) #and (os.name == "nt")
buildPath = "/builds" if shortBuildPath else "./builds"

# create a directory, if none exists
os.makedirs(buildPath, exist_ok=True)

inheritStr = "[from environment]"
print("Build Environment:")
print("    CI configuration: {}".format(sys.argv[1]))
print("    BUILD_VERSION: {} {}".format(os.environ['BUILD_VERSION'], inheritStr if buildVerInherit else ""))
print("    CONDARC path: {} {}".format(os.environ.get('CONDARC', ""), inheritStr if condarcInherit else "[not set]"))
print("")

with open(sys.argv[1], "rt") as yamlfile:
    yobj = yaml.safe_load(yamlfile)

params = ["conda-recipe"]
params += ["-m", sys.argv[1]]
params += ["--croot", buildPath]
params += ["--no-test"]
params += ["--no-anaconda-upload"]

# forward all additional parameters
if len(sys.argv) > 2:
    params += sys.argv[2:]

cmd = ["conda", "build"] + params
print(cmd)
proc = subprocess.run(cmd)
if shortBuildPath:
    # move builds folder back to work directory
    os.rename(buildPath, "./builds")
sys.exit(proc.returncode)
