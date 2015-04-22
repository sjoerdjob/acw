class Type(object):
    def __init__(self, default=None):
        if default is not None:
            if not self.validate(default):
                raise ValueError
            self.default = default


class IntegerType(Type):
    def validate(self, value):
        return isinstance(value, (int, long))

    def loads(self, raw):
        return int(raw)

    def dumps(self, val):
        return str(val)
