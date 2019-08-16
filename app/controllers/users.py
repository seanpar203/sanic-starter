""" User controllers using Sanic Class based views. """

from sanic.response import json
from sanic.views import HTTPMethodView

from app.database import scoped_session, Session
from app.models.users import User


class UserController(HTTPMethodView):
    """ Handles User CRUD operations. """

    async def get(self, request):
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
        # Gets all users in DB.
        with scoped_session() as session:
            users = session.query(User).all()

        return json({'users': users})

    async def post(self, request):
        """ Creates a new user based on the `email` key

        Args:
            request (object): contains data pertaining request.

        Returns:
            json: containing key `msg` with success info & email.
        """
        # Get email key from json request.
        email = request.json.get('email')

        # Create new user.
        with scoped_session() as session:
            user = User(email=email)
            session.add(user)

        # Return json response.
        return json({'msg': 'Successfully created {}'.format(email)})
