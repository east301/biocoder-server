#!/bin/bash
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

set -e

export C_FORCE_ROOT=true

/opt/biocoder/docker/wait-mysql.py
exec celery -A biocoder worker --concurrency 1 --no-color --loglevel=INFO
