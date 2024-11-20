class AppConfig:
    def __init__(self, config):
        self.app_port = config.get('app', 'APP_PORT', fallback=9000)
        self.debug = config.getboolean('app', 'DEBUG', fallback=False)

    def __repr__(self):
        return f"AppConfig(app_port={self.app_port}, debug={self.debug})"