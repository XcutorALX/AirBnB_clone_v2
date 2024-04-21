#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import models
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60),
        ForeignKey('cities.id'),
        nullable=False
        )
    user_id = Column(
        String(60),
        ForeignKey('users.id'),
        nullable=False
        )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    place_amenity = Table(
        'place_amenity',
        Base.metadata,
        Column(
            'place_id',
            String(60),
            ForeignKey('places.id'),
            primary_key=True,
            nullable=False
            ),
        Column(
            'amenity_id',
            String(60),
            ForeignKey('amenities.id'),
            primary_key=True,
            nullable=False
            )
        )

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete"
            )
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False
            )
    else:
        @property
        def reviews(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.review import Review
            reviews = storage.all(Review)
            return [review for review in reviews.values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.amenity import Amenity
            amenities = storage.all(Amenity)
            return [amenity for amenity in amenities.values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter attribute in case of file storage"""
            if type(obj).__name__ == 'Amenity':
                self.amenity_ids.append(obj.id)
