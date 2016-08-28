#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from django.utils.deprecation import MiddlewareMixin
from debug_toolbar.middleware import DebugToolbarMiddleware as DjangoDebugToolbarMiddleware


# ================================================================================
# middleware
# ================================================================================

class DebugToolbarMiddleware(MiddlewareMixin, DjangoDebugToolbarMiddleware):
    """Borrowed from　https://github.com/jazzband/django-debug-toolbar/issues/853"""
    pass
