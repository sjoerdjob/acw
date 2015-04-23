from nose.tools import raises

from acw.types import Type


class FakeType(Type):
    def validate(self, val):
        return isinstance(val, int) and 0 <= val <= 3

    def _dumps(self, val):
        return int(val)


def test_type_valid_default():
    t = FakeType(2)
    assert t.default == 2


@raises(ValueError)
def test_type_invalid_default():
    FakeType(4)


@raises(AttributeError)
def test_type_get_unset_default():
    t = FakeType()
    t.default
