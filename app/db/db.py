from ..config.config import Config

class Database:

    @classmethod
    def get_session(cls):
        return Config().database_config.session_factory()
