from sqlalchemy import (
    Column, String, Integer,
    Sequence, DateTime, Date, Boolean
)

from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    # Authentication Attributes.
    email = Column(String(255))
    token_expires = Column(DateTime)
    perishable_token = Column(String(255), unique=True)

    # Personal Attributes.
    birthday = Column(Date())
    first_name = Column(String(35))
    last_name = Column(String(35))

    # Permission Based Attributes.
    is_active = Column(Boolean, default=False)

    # Methods

    def __repr__(self):
        return '<User: a user object>'
