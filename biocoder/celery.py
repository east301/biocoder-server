#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from __future__ import absolute_import


# ================================================================================
# configures settings module path
# ================================================================================

from .apps.common.config import configure_settings_module_path  # NOQA

configure_settings_module_path()


# ================================================================================
# loads celery
# ================================================================================

from celery import Celery           # NOQA
from django.conf import settings    # NOQA

app = Celery('biocoder')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
