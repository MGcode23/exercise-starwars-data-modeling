import enum
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    favorites = relationship("Favorite", backref="user", lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    climate = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    favorite_planets = relationship("Favorite", back_populates="planet")
    characters = relationship("Character", secondary="character_planet_association")
    starships = relationship("Starship", secondary="starship_planet_association")

class Character(Base):
    __tablename__="character"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    height = Column(String(50), nullable=False)
    mass = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    favorite_characters = relationship("Favorite", back_populates="character")
    planets = relationship("Planet", secondary="character_planet_association")

class Starship(Base):
    __tablename__="starship"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    length = Column(String(50), nullable=False)
    crew = Column(String(50), nullable=False)
    favorite_starships = relationship("Favorite", back_populates="starship")
    planets = relationship("Planet", secondary="starship_planet_association")

character_planet_association = Table('character_planet_association', Base.metadata,
    Column('character_id', Integer, ForeignKey('character.id')),
    Column('planet_id', Integer, ForeignKey('planet.id'))
)

starship_planet_association = Table('starship_planet_association', Base.metadata,
    Column('starship_id', Integer, ForeignKey('starship.id')),
    Column('planet_id', Integer, ForeignKey('planet.id'))
)

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))
    planet = relationship("Planet", back_populates="favorite_planets")
    character = relationship("Character", back_populates="favorite_characters")
    starship = relationship("Starship", back_populates="favorite_starships")
    
    def add_favorites():
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
