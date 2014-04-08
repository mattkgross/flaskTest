from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
 
engine = create_engine('sqlite:///tubes.db', echo=True)
Base = declarative_base()
 
########################################################################
class Tubes(Base):
    """"""
    __tablename__ = "tubes"
 
    id = Column(Integer, primary_key=True)
    diameter = Column(Integer)
    durability = Column(String)
    usage = Column(String)
    pic_url = Column(String)
 
    #----------------------------------------------------------------------
    def __init__(self, diameter, durability, usage, pic_url):
        """"""
        self.diameter = diameter
        self.durability = durability
        self.usage = usage
        self.pic_url = pic_url
 
# create tables
Base.metadata.create_all(engine)