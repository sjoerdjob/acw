class Type(object):
    pass


class IntegerType(Type):
    def __init__(self, default=None):
        if default is not None:
            if not isinstance(default, (int, long)):
                raise ValueError
            self.default = default

    def loads(self, raw):
        return int(raw)

    def dumps(self, val):
        return str(val)
