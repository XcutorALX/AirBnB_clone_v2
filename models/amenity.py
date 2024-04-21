#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    @staticmethod
    def places_relationship():
        from models.place_amenity import place_amenity
        return relationship("Place",
                            secondary=place_amenity,
                            back_populates="amenities")
