#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan"
            )

    else:
        name = ""

        @property
        def cities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.city import City
            cities = storage.all(City)
            return [city for city in cities.values() if
                    city.state_id == self.id]
