#!/usr/bin/env python3
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import argparse
import sys
import time

from django.db import OperationalError, connection

from biocoder.apps.common.config import configure_settings_module_path


def main():
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', type=int, default=1)
    parser.add_argument('--max-count', type=int, default=60)
    args = parser.parse_args()

    #
    configure_settings_module_path()

    #
    connected = False
    for x in range(1, args.max_count + 1):
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
                connected = True
                break

        except OperationalError:
            print('Waiting mysql ({}) ...'.format(x), file=sys.stderr)
            time.sleep(args.interval)

    #
    return 0 if connected else 1


if __name__ == '__main__':
    sys.exit(main())
