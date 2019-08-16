""" Module for managing tasks through a simple cli interface. """
# Libraries
from manager import Manager

from app import run_app

# Constants.
manager = Manager()


@manager.command
def run():
    """ Starts server on port 8000. """
    run_app()

if __name__ == '__main__':
    manager.main()
