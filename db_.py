import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Leader(Base):
    __tablename__ = 'leader'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    password = Column(String(250), nullable = False)
    rating = Column(String(250), nullable = False)
