from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_enginie

Base = declarative_base()

class Dev():

    __tablename__ = "dev"

    id = Column(Integer, primary_key=True)
    created_at = Column(Integer)
    updated_at = Column(Integer)
    deleted = Column(Boolean)

    