#!/usr/bin/python3
"""
This module contains a DBStorage class
"""

from sqlalchemy import create_engine
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import sessionmaker
from os import getenv
import models

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the DBStorage instance
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}?charset=latin1'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True, encoding="latin1",
                                      connect_args={"charset": "latin1"},)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary of all objects in the database
        """

        objs = {}
        if cls:
            if type(cls) is str:
                cls = models.classes[cls]
            for obj in self.__session.query(cls).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for key, cls in models.classes.items():
                if key != 'BaseModel':
                    for obj in self.__session.query(cls).all():
                        objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """
        Adds a new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes an object from the database
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and initializes a session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """
            call remove() method on the private session attribute
            (self.__session) tips or close() on the class Session
        """

        self.__session.close()
