#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import jsonschema
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.exceptions import SuspiciousOperation


# ================================================================================
# validation
# ================================================================================

class JSONSchemaValidationMixin(object):
    def dispatch(self, request, *args, **kwargs):
        #
        if request.method == 'POST':
            try:
                jsonschema.validate(request.POST, self.schema)
            except ValueError as exc:
                raise SuspiciousOperation('Failed to validate request parameters.') from exc

        #
        return super(JSONSchemaValidationMixin, self).dispatch(request, *args, **kwargs)


class DjangoFormValidationMixin(object):
    def __init__(self, *args, **kwargs):
        super(DjangoFormValidationMixin, self).__init__(*args, **kwargs)
        self.form_validator = None

    def dispatch(self, request, *args, **kwargs):
        #
        if request.method == 'POST':
            self.form_validator = self.form_validator_class(request.POST, request.FILES)
            if not self.form_validator.is_valid():
                raise SuspiciousOperation('Failed to validate request parameters.')

        #
        return super(DjangoFormValidationMixin, self).dispatch(request, *args, **kwargs)


# ================================================================================
# authentication
# ================================================================================

class StaffUserRequiredMixin(LoginRequiredMixin, StaffuserRequiredMixin):
    pass
