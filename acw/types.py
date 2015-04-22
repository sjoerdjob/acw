class Type(object):
    def __init__(self, default=None):
        if default is not None:
            if not self.validate(default):
                raise ValueError
            self.default = default

    def dumps(self, val):
        if not self.validate(val):
            raise ValueError
        else:
            return self._dumps(val)


class IntegerType(Type):
    def validate(self, value):
        return isinstance(value, (int, long))

    def loads(self, raw):
        return int(raw)

    def _dumps(self, val):
        return str(val)


class StringType(Type):
    def validate(self, value):
        return isinstance(value, str)

    def loads(self, raw):
        return raw

    def _dumps(self, val):
        return val
