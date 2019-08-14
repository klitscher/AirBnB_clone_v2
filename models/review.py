#!/usr/bin/python3
"""This is the review class"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id
        user_id: user id
        text: review description
    """
    __tablename__ = 'reviews'
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship(
        'User', back_populates='reviews') # cascade?
