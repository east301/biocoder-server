#!/usr/bin/env python3
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import argparse

import django
from django.db import IntegrityError


def main():
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', default='admin')
    parser.add_argument('--password', default='password')
    parser.add_argument('--show-error', action='store_true', default=False)
    args = parser.parse_args()

    #
    django.setup()

    #
    from django.contrib.auth.models import User

    try:
        User.objects.create_user(
            username=args.username, password=args.password, is_staff=True, is_superuser=True)
    except IntegrityError:
        if args.show_error:
            raise


if __name__ == '__main__':
    main()
