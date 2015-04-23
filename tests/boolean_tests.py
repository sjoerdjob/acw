from nose.tools import raises

from acw.types import BooleanType


def test_bool_type_loads_boolean():
    t = BooleanType()
    assert t.loads("True")
    assert t.loads("t")
    assert not t.loads("False")
    assert not t.loads("f")


@raises(ValueError)
def test_bool_type_loads_nonboolean():
    t = BooleanType()
    t.loads("foo")


def test_bool_type_dumps():
    t = BooleanType()
    assert t.dumps(True) == "True"
    assert t.dumps(False) == "False"


@raises(ValueError)
def test_bool_type_dumps_nonboolean():
    t = BooleanType()
    t.dumps(1)
