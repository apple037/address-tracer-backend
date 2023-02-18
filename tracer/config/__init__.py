import os
import logging

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG
)
LOGGER = logging.getLogger()


def load_config():
    """
    Load a config class
    """

    os.environ['PROFILE'] = 'LOCAL'
    mode = os.environ.get('PROFILE', 'LOCAL')
    LOGGER.info('server profile：{}'.format(mode))
    try:
        if mode == 'DEV':
            from .local_config import LocalConfig
            return LocalConfig
        else:
            from .local_config import LocalConfig
            return LocalConfig
    except ImportError:
        from .config import Config
        return Config


CONFIG = load_config()
