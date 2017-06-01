import ConfigParser


class Configuration(object):
    _configuration = None

    @classmethod
    def _load_configuration(cls):
        config_dict = {}
        config = ConfigParser.ConfigParser()
        config.read('data/downloader.cfg')
        config_dict['data_path'] = config.get('main', 'data_path')
        cls._configuration = config_dict

    @classmethod
    def get(cls):
        if cls._configuration is None:
            cls._load_configuration()
        return cls._configuration

    @classmethod
    def get_prop(cls, prop):
        """Get the property value by the name."""
        value = cls.get().get(prop)
        return value
