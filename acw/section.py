from ConfigParser import NoSectionError, NoOptionError


class ConfigSection(object):
    def __init__(self, config):
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
