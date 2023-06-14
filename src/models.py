import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(40), unique=True, nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    height = Column(String(10), nullable=False)
    mass = Column(String(10), nullable=False)
    gender = Column(String(10))

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    climate = Column(String(10), nullable=False)
    gravity = Column(String(10), nullable=False)
    terrain = Column(String(20), nullable=False)

class Starship(Base):
    __tablename__ = "starship"
    id = Column(Integer, primary_key=True)
    name = Column(String(70), nullable=False)
    model = Column(String(10), nullable=False)
    manufacturer = Column(String(10), nullable=False)
    hyperdrive_rating = Column(String(20), nullable=False)

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    starship_id = Column(Integer, ForeignKey("starship.id"))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
