#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import os
import sys

from django.core.exceptions import ImproperlyConfigured


# ================================================================================
# auto configuration
# ================================================================================

def configure_settings_module_path():
    #
    if 'DJANGO_SETTINGS_MODULE' in os.environ:
        return

    #
    settings_py_path = os.path.join('/', 'etc', 'biocoder', 'biocoder_settings.py')

    if os.path.exists(settings_py_path):
        sys.path.insert(0, os.path.dirname(settings_py_path))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'biocoder_settings'

    else:
        raise ImproperlyConfigured(
            'DJANGO_SETTINGS_MODULE is not set, '
            'and /etc/biocoder/biocoder_settings.py is not found.')
