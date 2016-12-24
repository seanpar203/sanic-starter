import os
from sanic import Sanic

# Prepend '/api' before every route.
BP_OPTIONS = {'url_prefix': '/api'}


def create_app():
    """ Function for bootstrapping sanic app. """
    app = Sanic(__name__)

    # Register blueprints.
    from app.controllers.users import user
    app.blueprint(user, **BP_OPTIONS)

    print(app.router)
    app.run(host='0.0.0.0', port=8000, debug=True, workers=os.cpu_count())
