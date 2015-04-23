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


@raises(ValueError)
def test_int_type_dumps_noninteger():
    t = IntegerType()
    t.dumps("1")
