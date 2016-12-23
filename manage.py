""" Module for managing tasks through a simple cli interface. """

# Modules
from manager import Manager

# App
from app import create_app

# Constants.
manager = Manager()


@manager.command
def run():
    """ Starts server on port 8000. """
    create_app()


if __name__ == '__main__':
    manager.main()
