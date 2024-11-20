import configparser
import os

from .database.DatabaseConfig import DatabaseConfig
from .app.AppConfig import AppConfig


def init_config():
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

    ini_file = os.path.join(os.path.dirname(__file__), 'config.ini')

    with open(ini_file, 'r') as cfg_file:
        cfg_env_txt = os.path.expandvars(cfg_file.read())

    config.read_string(cfg_env_txt)

    database_config = DatabaseConfig(config)
    app_config = AppConfig(config)

    return database_config, app_config