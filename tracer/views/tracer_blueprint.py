from sanic import Blueprint, response

tracer_bp = Blueprint('tracer_blueprint', url_prefix='tracer')


@tracer_bp.get('/ping')
async def ping(request):
    return response.text('pong')
