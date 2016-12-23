""" Module for managing tasks through a simple cli interface. """

# Modules
from manager import Manager

# App
from app import create_app
from models import Base

# Constants.
manager = Manager()


@manager.command
def run():
    """ Starts server on port 8000. """
    create_app()

def init_db():
    Base.metadata.create_all()

if __name__ == '__main__':
    manager.main()
