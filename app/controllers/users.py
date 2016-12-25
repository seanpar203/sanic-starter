""" User controllers using Sanic Class based views. """
from sanic.response import json
from sanic.views import HTTPMethodView
from sqlalchemy.sql import insert, select

from app.database import db
from app.models.users import User


class UserController(HTTPMethodView):
    """ Handles User CRUD operations. """

    def get(self, request):
        """ Gets all users in the DB

        Args:
            request (object): contains data pertaining request.

        Notes:
            Realistically There would be some form of authentication in place
            Like a Token to grab the Auth Header value and return a specific
            user based on Token. Although for the purpose of brevity this route
            will just return all users in the database.

        Returns:
            json: containing list of users under the `users` key.
        """
        # Prepare stmt.
        stmt = select([User])

        # Prepare connection & execute stmt.
        conn = db.connect()
        users = [dict(user) for user in conn.execute(stmt).fetchall()]
        conn.close()

        # Return json response.
        return json({'users': users})

    def post(self, request):
        """ Creates a new user based on the `email` key

        Args:
            request (object): contains data pertaining request.

        Returns:
            json: containing key `msg` with success info & email.
        """
        # Get email key from json request.
        email = request.json.get('email')

        # Prepare stmt.
        stmt = insert(User).values(email=email)

        # Prepare connection & execute stmt.
        conn = db.connect()
        conn.execute(stmt)
        conn.close()

        # Return json response.
        return json({'msg': 'Successfully created {}'.format(email)})
