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



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(40), unique=True, nullable=False)
    username = Column(String(30), nullable=False)
    password = Column(String(60), nullable=False)

class Post(Base):
     __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"))

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    post_id = Column(Integer, ForeignKey("post.id"))


# class Parent(Base):
#     __tablename__ = 'parent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     child = relationship('Child', back_populates='parent', uselist=False)


# class Child(Base):
#     __tablename__ = 'child'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     parent_id = Column(Integer, ForeignKey("parent.id"))



#########################################################

# class Post(Base):
#     __tablename__ = 'post'
#     id = Column(Integer, primary_key=True)
#     description = Column(Text, nullable=False)
#     user_id = Column(Integer, ForeignKey("user.id"))

#########################################################

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
