from sanic import Blueprint
from sanic.response import json
from sqlalchemy import insert

from app.database import db
from app.models.users import User

user = Blueprint('user')


@user.route('/', methods=['GET'])
async def foo(request):
    stmt = insert(User).values(email='some@gmail.com')
    conn = db.connect()
    conn.execute(stmt)
    conn.close()
    return json({'msg': 'Successfully created a user.'})
