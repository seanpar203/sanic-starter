from sanic_envconfig import EnvConfig


class Config(EnvConfig):
    DEBUG: bool = True
    AUTORELOAD: bool = True
    HOST: str = '0.0.0.0'
    PORT: int = 34785
    KEEP_ALIVE: bool = True
    WORKERS: int = 1
    DATABASE_URL: str = 'sqlite:///app.db'
    REQUEST_TIMEOUT: int = 60
    ENVIRONMENT_NAME: str = 'development'
