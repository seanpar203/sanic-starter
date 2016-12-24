""" Module for handling all database models. """
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import models to allow easy Alembic autogenerate.
from app.models.users import User
