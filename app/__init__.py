""" App entry point. """
from sanic import Sanic
from config import Config


def create_app(config=Config):
    """ Function for bootstrapping sanic app. """
    app = Sanic(__name__)
    app.config.from_object(config)

    # Register Blueprints/Views.
    from app.controllers.users import UserController
    app.add_route(UserController.as_view(), '/api/user')


def run_app(config=Config):
    app = create_app(config)

    app.run(
        host=config.HOST, port=config.PORT,
        debug=config.DEBUG, access_log=config.DEBUG, workers=config.WORKERS)
