from nose.tools import raises

from acw.types import IntegerType


def test_int_type_loads_integer():
    t = IntegerType()
    assert t.loads("1") == 1


@raises(ValueError)
def test_int_type_loads_noninteger():
    t = IntegerType()
    t.loads("foo")


def test_int_type_dumps():
    t = IntegerType()
    assert t.dumps(1) == "1"


def test_int_type_default_set():
    t = IntegerType(1)
    assert t.default == 1


@raises(AttributeError)
def test_int_type_default_unset():
    t = IntegerType()
    t.default


@raises(ValueError)
def test_int_type_default_wrong_type():
    IntegerType("1")
