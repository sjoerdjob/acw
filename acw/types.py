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

    def validate(self, value):
        raise NotImplementedError

    def _dumps(self, val):
        raise NotImplementedError


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


class BooleanType(Type):
    TRUE_VALUES = ('true', 't', 'yes', 'y', '1')
    FALSE_VALUES = ('false', 'f', 'no', 'n', '0')


    def validate(self, value):
        # Even though it is normal to consider just any value as proper input,
        # it is my belief that here it is best to explicitly require boolean
        # values.
        return isinstance(value, bool)

    def loads(self, raw):
        lower_raw = raw.lower()
        if lower_raw in self.TRUE_VALUES:
            return True
        if lower_raw in self.FALSE_VALUES:
            return False
        raise ValueError("Value {} does not look like a boolean".format(raw))

    def _dumps(self, val):
        return str(val)
