import os

from sanic import Sanic
from sanic_ext import Extend
from tracer.config import CONFIG, LOGGER
from tracer.views import tracer_bp

app = Sanic(__name__)
app.blueprint(tracer_bp)
app.config.CORS_ORIGINS = "http://127.0.0.1:5173,http://localhost:5173"
Extend(app)


@app.listener('before_server_start')
def init_cache(application):
    LOGGER.info("Running with profile: {}".format(os.environ['PROFILE']))
    LOGGER.info("Reading config")
    LOGGER.info('CONFIG config: {}'.format(CONFIG))
    app.update_config(CONFIG)
    REDIS_DICT = CONFIG.REDIS_DICT
    LOGGER.info('REDIS config: {}'.format(REDIS_DICT))
    MYSQL_DICT = CONFIG.MYSQL_DICT
    LOGGER.info('MYSQL config: {}'.format(MYSQL_DICT))
    LOGGER.info('CORS_ALLOW_HEADERS config: {}'.format(app.config.CORS_ORIGINS))


if __name__ == "__main__":
    workers = 1
    app.run(port=9999, workers=workers, debug=CONFIG.DEBUG)
