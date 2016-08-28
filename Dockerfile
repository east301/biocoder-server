#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

FROM python:3.5-slim
MAINTAINER east301 <me@east301.net>

ENV VERSION 0.0.0

RUN mkdir -p /opt/biocoder
ADD ./packaing/docker /opt/biocoder/docker

RUN apt-get update\
    && apt-get install -y file gcc\
    && pip install /opt/biocoder/docker/biocoder-$VERSION-py3-none-any.whl\
    && pip install -r /opt/biocoder/docker/requirements-production.txt\
    && apt-get remove -y gcc\
    && apt-get autoremove -y\
    && apt-get clean -y\
    && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
