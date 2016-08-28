#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import pkg_resources


try:
    VERSION = pkg_resources.require('biocoder')[0].version
except:
    VERSION = None

GIT_REVISION = '{{ git_revision }}'
