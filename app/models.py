from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base
from sqlalchemy import Column, Integer,String,Boolean
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__= "posts"

    id=Column(Integer, primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content= Column(String,nullable=False)
    Published = Column(Boolean,server_default="True",nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))