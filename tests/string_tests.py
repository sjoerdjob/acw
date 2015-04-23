from nose.tools import raises

from acw.types import StringType


def test_string_type_loads_string():
    t = StringType()
    assert t.loads("hello") == "hello"


@raises(ValueError)
def test_string_type_loads_nonstring():
    t = StringType()
    t.dumps(1)


def test_string_type_dumps():
    t = StringType()
    assert t.dumps("hello") == "hello"
