from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base
from eralchemy2 import render_er

Base = declarative_base()


class Planet(Base): 
    __tablename__ = 'planete'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Description = Column(String(500), nullable=True)
    Planet_pic = Column(String(512), nullable=True)

class Character(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Description = Column(String(500), nullable=True)
    Character_pic = Column(String(512), nullable=True)

class Favorite(Base): 
    __tablename__ = 'favorite'
    ID = Column(Integer, primary_key=True)
    Character_ID = Column(String(50), ForeignKey('characters.id'))
    Planet_ID = Column(String(50), ForeignKey('planete.id'))    
    User_ID = Column(String(250), ForeignKey('user.id'))

class Register(Base): 
    __tablename__ = 'register'
    ID = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Username = Column(String(25), unique=True)
    Email = Column(String(250), unique=True)
    Password = Column(String(50), nullable=False)

class LogIn(Base):
    __tablename__ = 'login'
    ID = Column(Integer, primary_key=True)
    DateTime = Column(DateTime(25))
    Success = Column(Boolean(50), default=False)
    User_ID = Column(String(250), ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    Register_ID = Column(String(250), ForeignKey('register.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')