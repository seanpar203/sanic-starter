from sanic.response import json
from sanic import Blueprint

user = Blueprint('user')


@user.route('/', methods=['GET'])
async def foo(request):
    return json({'msg': 'hi from blueprint'})
