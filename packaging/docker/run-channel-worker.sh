#!/bin/bash
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

set -e

/opt/biocoder/docker/wait-mysql.py
exec biocoder-cli runworker --no-color
