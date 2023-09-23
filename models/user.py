#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    This is the class for user
    """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    """
    # Relationships with other classes (Place and Review)
    # using SQLAlchemy's ORM
    """
    places = relationship("Place", cascade="all, delete, delete-orphan", backref="user")
    reviews = relationship("Review", cascade="all, delete, delete-orphan", backref="user")
