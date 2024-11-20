import psycopg2


class DatabaseConfig:
    def __init__(self, config):
        self.db_name = config.get('database', 'DB_NAME', fallback='default_db')
        self.db_user = config.get('database', 'DB_USER', fallback='default_user')
        self.db_password = config.get('database', 'DB_PASSWORD', fallback='default_password')
        self.db_host = config.get('database', 'DB_HOST', fallback='localhost')
        self.db_port = config.get('database', 'DB_PORT', fallback=5432)

    def __repr__(self):
        return f"DatabaseConfig(db_name={self.db_name}, db_user={self.db_user}, db_password={self.db_password}, db_host={self.db_host}, db_port={self.db_port})"

    def connect(self):
        try:
            conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            print("Conexão com o PostgreSQL bem-sucedida!")
            conn.close()
        except Exception as e:
            print(f"Erro de conexão: {e}")