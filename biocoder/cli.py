#!/usr/bin/env python3
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import sys

from django.core.management import execute_from_command_line

from .apps.common.config import configure_settings_module_path


def main():
    configure_settings_module_path()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
