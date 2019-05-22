#!/usr/bin/env python

import subprocess
import sys
import re

from githooks import args

files = [f for f in args.pre_commit().files if re.match('.*\.py$', f)]

if files:
    sys.exit(subprocess.call(['flake8'] + files))
