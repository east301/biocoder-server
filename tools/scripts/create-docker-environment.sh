#!/bin/bash
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

source=$(cd $(dirname "$0")/../.. && pwd)
destination=$1

mkdir -p $destination/config

cp $source/docker-compose.yml $destination/docker-compose.yml
cp $source/docker/env.template $destination/env
cp $source/docker/biocoder_settings_template.py $destination/config/biocoder_settings.py
