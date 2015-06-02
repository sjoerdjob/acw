from ConfigParser import NoSectionError, NoOptionError

from .types import Type


def _get_fields(attributes):
    fields = {}
    for key, value in attributes.items():
        if isinstance(value, Type):
            fields[key] = value
            del attributes[key]
    return fields


def _get_name(name):
    if name.endswith('ConfigSection'):
        # Strip off the 'ConfigSection' part.
        name = name[:-13]

    # We may want to do some PascalCase -> SnakeCase conversion here later.
    # For now, this suffices.
    return name.lower()


class _ConfigSectionMeta(type):
    def __new__(mcs, name, bases, attrs):
        attrs['_options'] = _get_fields(attrs)
        attrs.setdefault('_name', _get_name(name))
        return super(_ConfigSectionMeta, mcs).__new__(mcs, name, bases, attrs)


class ConfigSection(object):
    __metaclass__ = _ConfigSectionMeta

    def __init__(self, name, config):
        self.__dict__['_name'] = name
        self.__dict__['_config'] = config

    def __getattr__(self, option):
        assert option in self._options, option
        option_desc = self._options[option]
        try:
            raw_value = self._config.get(self._name, option)
        except (NoSectionError, NoOptionError):
            try:
                return option_desc.default
            except AttributeError:
                # Return attribute-error for option name instead of 'default'.
                raise AttributeError(option)
        else:
            return option_desc.loads(raw_value)

    def __setattr__(self, option, value):
        assert option in self._options, option
        option_desc = self._options[option]
        raw_value = option_desc.dumps(value)
        if not self._config.has_section(self._name):
            self._config.add_section(self._name)
        self._config.set(self._name, option, raw_value)
