import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'  
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship('Person') 

class FavoriteItem(Base):
    __tablename__ = 'favorite_items'  
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True, nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)

class User(Base):
    __tablename__ = 'user'  
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    favorites = relationship('FavoriteItem', back_populates='user')

class Planet(Base):  
    __tablename__ = 'planets' 
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=True)
    name = Column(String(250), nullable=True)
    population = Column(Integer)
    favorites = relationship('FavoriteItem', backref='planet')  

class Character(Base):  
    __tablename__ = 'characters' 
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    last_name = Column(String(250))
    height = Column(Float)
    favorites = relationship('FavoriteItem', backref='character')  

    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')
