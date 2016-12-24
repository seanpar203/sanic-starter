""" Module for managing tasks through a simple cli interface. """
# Libraries
from manager import Manager

from app import create_app
from app.models import create_db

# Constants.
manager = Manager()


@manager.command
def run():
    """ Starts server on port 8000. """
    create_app()


@manager.command
def init_db():
    """ Creates all the tables. """
    create_db()


if __name__ == '__main__':
    manager.main()
