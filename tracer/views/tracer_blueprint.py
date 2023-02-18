from sanic import Blueprint, response

tracer_bp = Blueprint('tracer_blueprint', url_prefix='tracer')


@tracer_bp.get('/ping')
async def ping(request):
    return response.text('pong')


@tracer_bp.get('/test')
async def json(request):
    return response.json({'ping': 'pong'})


@tracer_bp.get('/owner')
async def json(request):
    return response.json({'name': 'JasperFan'})
