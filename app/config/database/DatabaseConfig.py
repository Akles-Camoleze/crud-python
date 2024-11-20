from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConfig:
    def __init__(self, config):
        self.db_name = config.get('database', 'DB_NAME', fallback='default_db')
        self.db_user = config.get('database', 'DB_USER', fallback='default_user')
        self.db_password = config.get('database', 'DB_PASSWORD', fallback='default_password')
        self.db_host = config.get('database', 'DB_HOST', fallback='localhost')
        self.db_port = config.get('database', 'DB_PORT', fallback=5432)
        self.db_url = config.get('database', 'DB_URL')
        self._engine = create_engine(self.db_url, pool_pre_ping=True)
        self._session_factory = sessionmaker(bind=self._engine)

    def __repr__(self):
        return f"DatabaseConfig(db_name={self.db_name}, db_user={self.db_user}, db_password={self.db_password}, db_host={self.db_host}, db_port={self.db_port})"

    def session_factory(self):
        return self._session_factory()