#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.amenity import Amenity
import os
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(
            String(60),
            ForeignKey('cities.id', ondelete='CASCADE', onupdate='CASCADE'),
            nullable=False
            )
        user_id = Column(
            String(60),
            ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'),
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

        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete-orphan"
            )
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            backref="place_amenities",
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
