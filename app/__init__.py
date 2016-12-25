""" App entry point. """
import os
import asyncio

import uvloop
from sanic import Sanic


def create_app():
    """ Function for bootstrapping sanic app. """
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    app = Sanic(__name__)

    # Register Blueprints/Views.
    from app.controllers.users import UserController
    app.add_route(UserController(), '/api/user')

    app.run(debug=True, workers=os.cpu_count())
