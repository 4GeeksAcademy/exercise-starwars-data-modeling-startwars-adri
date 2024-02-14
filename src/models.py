import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    _tablename_ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    _tablename_ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class FavoriteItem(Base):
    _tablename_ = 'favorite_items'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)
class User(Base):
    _tablename_ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship('FavoriteItem', back_populates='user')
class Planets(Base):
    _tablename_ = 'planets'
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    population = Column(Integer)
    favorite_id = relationship('FavoriteItem', backref='planets')
class Characters(Base):
    _tablename_ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    height = Column(Float)
    favorite_id = relationship('FavoriteItem', backref='characters')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
