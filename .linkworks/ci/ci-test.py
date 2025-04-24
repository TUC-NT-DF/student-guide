#!/usr/bin/env python3
#
# NOTE: This script has been automatically generated.
# Any changes will be lost when the configuration is rerendered!

import sys
import os
import yaml
import subprocess
import glob

with open(sys.argv[1], "rt") as yamlfile:
    yobj = yaml.safe_load(yamlfile)

bldpath = "builds"    # same as in ci-build.py
platformdirs = yobj["target_platform"]

# param1 - parameters before package name
# param2 - parameters after package name
params1 = ["-m", sys.argv[1]]
params2 = []
pkgs = []
for platform in platformdirs:
    pkgs += glob.glob(os.path.join(bldpath, platform, "*.tar.bz2"))
    pkgs += glob.glob(os.path.join(bldpath, platform, "*.conda"))

# forward all additional parameters
if len(sys.argv) > 2:
    params2 += sys.argv[2:]

for pkg in pkgs:
    cmd = ["conda", "build", "--test"] + params1 + [pkg] + params2
    print(cmd)
    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        sys.exit(proc.returncode)

if len(pkgs) == 0:
    print("No packages to test.")
sys.exit(0)
