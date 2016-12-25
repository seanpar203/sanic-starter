""" This module exports the database engine.

Notes:
     This makes importing the db anywhere in the app easy.
     Aswell as grabbing a connection from the pool with
     `db.connect()`.
"""
import os
from sqlalchemy import create_engine

db = create_engine(os.environ['DATABASE_URL'])
