#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from django.conf import settings
from django.conf.urls import url


urlpatterns = []


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    urlpatterns += [url(r'^admin/', admin.site.urls)]
