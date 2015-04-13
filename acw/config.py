from .section import ConfigSection


def get_fields(attributes):
    fields = {}
    for key, value in attributes.items():
        print key, value
        if isinstance(value, type) and issubclass(value, ConfigSection):
            fields[key] = value
            del attributes[key]
    return fields


class ConfigMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['_sections'] = get_fields(attrs)
        return super(ConfigMeta, cls).__new__(cls, name, bases, attrs)


class Config(object):
    __metaclass__ = ConfigMeta

    def __init__(self, config):
        self._config = config

        # Initialize all the classes
        self._sections = {k: v(k, config) for k, v in self._sections.items()}

    def __getattr__(self, name):
        return self._sections[name]
