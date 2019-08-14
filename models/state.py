#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities = relationship between state and city tables.
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """returns list of Cities and some relationships"""
        cities_instances = []
        cities_dict = models.storage.all(City)
        for key, value in cities_dict.items():
            state.id == state_id
