import os
from sqlalchemy import create_engine

db = create_engine(os.environ['DATABASE_URL'])
