#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """returns list of Cities and some relationships"""
        return self.cities
