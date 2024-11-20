import configparser
import os
from .database.DatabaseConfig import DatabaseConfig
from .app.AppConfig import AppConfig

class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Config, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):  # Evita inicialização múltipla
            self._config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
            self._ini_file = os.path.join(os.path.dirname(__file__), 'config.ini')
            with open(self._ini_file, 'r') as cfg_file:
                cfg_env_txt = os.path.expandvars(cfg_file.read())
            self._config.read_string(cfg_env_txt)
            self._database_config = DatabaseConfig(self._config)
            self._app_config = AppConfig(self._config)
            self._initialized = True

    @property
    def database_config(self) -> DatabaseConfig:
        return self._database_config

    @property
    def app_config(self) -> AppConfig:
        return self._app_config
