#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(120), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
    """A Getter attr cities that returns the list of cities
    """
    from models import storage
    my_list = []
    extract_cities = storage.all(City).value()
    for city in extract_cities:
        if self.id == city.state_id:
            my_list.append(city)
    return my_list
