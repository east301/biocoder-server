#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from django.core.wsgi import get_wsgi_application

from .apps.common.config import configure_settings_module_path


configure_settings_module_path()
application = get_wsgi_application()
