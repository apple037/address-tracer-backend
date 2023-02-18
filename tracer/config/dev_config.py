import os
from .config import Config


class DevConfig(Config):
    HOST = '127.0.0.1'
    DEBUG = True
    MYSQL_DICT = dict(
        MYSQL_HOST=os.getenv('MYSQL_HOST', "127.0.0.1"),
        MYSQL_PORT=int(os.getenv('MYSQL_PORT', 3306)),
        MYSQL_USER=os.getenv('MYSQL_USER', 'root'),
        MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD', 'root'),
        MYSQL_DB=os.getenv('MYSQL_DB', 'address_tracer'),
    )

    REDIS_DICT = dict(
        IS_CACHE=True,
        REDIS_ENDPOINT=os.getenv('REDIS_ENDPOINT', "localhost"),
        REDIS_PORT=int(os.getenv('REDIS_PORT', 6379)),
        REDIS_PASSWORD=os.getenv('REDIS_PASSWORD', None),
        CACHE_DB=0,
        SESSION_DB=1,
        POOLSIZE=10,
    )
