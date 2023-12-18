#!/usr/bin/python3
"""
This file contains the class definition of a State.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    This State class.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City", backref="state", cascade="all, delete-orphan"
    )
