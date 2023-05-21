#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """ Review class to store review information """
    __tablename = "reviews"
    place_id = Column(String(50), ForeignKey('place.id'), nullable=False)
    user_id = Column(String(50), ForeignKey('user.id'), nullable=False)
    text = Column(String(1000), nullable=False)
