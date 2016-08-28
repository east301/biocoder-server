#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#


# ================================================================================
# stringify
# ================================================================================

def stringify_by(template):
    def add_stringify_method(klass):
        klass.__repr__ = lambda self: '<{}: {}>'.format(klass.__name__, template.format(_=self))
        klass.__str__ = lambda self: template.format(_=self)
        return klass

    return add_stringify_method
