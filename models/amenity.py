#!/usr/bin/python3
"""This is the amenity class"""
import os
from models.base_model import BaseModel, Base
from sqlalchmey import Column, String, Integer
from sqlalchemy.orm import relationship
from models.places import association_table


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place',
                                       secondary=place_amenity,
                                       back_populates='amenities')
    else:
        name = ""
