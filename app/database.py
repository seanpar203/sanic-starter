""" This module exports the database engine.

Notes:
     Using the scoped_session contextmanager is
     best practice to ensure the session gets closed
     and reduces noise in code by not having to manually
     commit or rollback the db if a exception occurs.
"""
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionORM
from sqlalchemy.engine import Engine


engine: Engine = None
Session: SessionORM = None


@contextmanager
def scoped_session():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def init(app):
    global engine, Session

    engine = create_engine(app.config.DATABASE_URL)
    # Session to be used throughout app.
    Session = sessionmaker(bind=engine, expire_on_commit=False)
