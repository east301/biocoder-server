#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit


# ================================================================================
# form helper
# ================================================================================

class CrispyFormsMixin(object):
    def __init__(self, *args, **kwargs):
        super(CrispyFormsMixin, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        submit_field = Submit('_submit', 'Submit')

        if hasattr(self, 'field_ordering'):
            fields = list(map(Field, self.field_ordering)) + [submit_field]
            self.helper.layout = Layout(*fields)
        else:
            self.helper.add_input(submit_field)
