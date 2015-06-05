from acw import Config
from acw.section import ConfigSection
from acw.types import IntegerType


from ConfigParser import ConfigParser
from StringIO import StringIO


class SillyConfigSection(ConfigSection):
    foo = IntegerType()
    bar = IntegerType(5)


class SillyConfig(Config):
    silly = SillyConfigSection


def test_config_get_integer():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
bar = 2
"""))
    c = SillyConfig(config)
    assert c.silly.foo == 1
    assert c.silly.bar == 2


def test_config_get_defaulted():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
"""))
    c = SillyConfig(config)
    assert c.silly.bar == 5


def test_set_integer_to_config():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
"""))
    c = SillyConfig(config)
    c.silly.bar = 2
    fp = StringIO()
    config.write(fp)
    assert fp.getvalue() == """
[silly]
foo = 1
bar = 2

""".lstrip(), "#" + fp.getvalue() + "#"


def test_valid_invalid():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
"""))
    c = SillyConfig(config)
    assert c.is_valid()
