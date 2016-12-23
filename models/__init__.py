import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def create_db():
    # Create engine.
    engine = create_engine(os.environ['DATABASE_URL'])

    # Import models
    from models.user import User

    # Create tables based on models.
    Base.metadata.create_all(bind=engine)
