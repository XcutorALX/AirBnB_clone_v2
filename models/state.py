#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete"
        )

    @property
    def cities(self):
        """Getter attribute in case of file storage"""
        from models import storage
        from models.city import City
        cities = storage.all(City)
        return [city for city in cities.values() if city.state_id == self.id]
