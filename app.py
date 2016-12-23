from sanic import Sanic


def create_app():
    """ Function for bootstrapping sanic app. """
    app = Sanic(__name__)
    app.run(host='0.0.0.0', port='8000', debug=True)
