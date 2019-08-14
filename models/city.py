#!/usr/bin/python3
"""This is the city class"""


from models.base_model import BaseModel, Base, Column, String, ForeignKey


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """

    __tablename__ = 'cities'
    state_id = ""
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
