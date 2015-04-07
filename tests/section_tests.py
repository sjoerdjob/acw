from acw.section import ConfigSection
from acw.types import IntegerType


from ConfigParser import ConfigParser
from StringIO import StringIO


class SillyConfigSection(ConfigSection):
    foo = IntegerType()
    bar = IntegerType(5)


def test_config_section_get_integer():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
bar = 2
"""))
    c = SillyConfigSection(config)
    assert c.foo == 1
    assert c.bar == 2


def test_config_section_get_defaulted():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
"""))
    c = SillyConfigSection(config)
    assert c.bar == 5


def test_set_integer_to_config():
    config = ConfigParser()
    config.readfp(StringIO("""
[silly]
foo = 1
"""))
    c = SillyConfigSection(config)
    c.bar = 2
    fp = StringIO()
    config.write(fp)
    assert fp.getvalue() == """
[silly]
foo = 1
bar = 2

""".lstrip(), "#" + fp.getvalue() + "#"
