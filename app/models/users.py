from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean
)

from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)

    # Authentication Attributes.
    email = Column(String(255), nullable=False)
    token_expires = Column(DateTime, nullable=True)
    perishable_token = Column(String(255), nullable=True, unique=True)

    # Personal Attributes.
    birthday = Column(Date, nullable=True)
    first_name = Column(String(35), nullable=True)
    last_name = Column(String(35), nullable=True)

    # Permission Based Attributes.
    is_active = Column(Boolean, default=False)

    # Methods

    def __repr__(self):
        return '<User: {}>'.format(self.id)
