from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Boolean

Base=declarative_base()
class TaskModel(Base):
    __tablename__="tasks"
    id=Column(Integer,primary_key=True,autoincrement=True)
    task=Column(String(250),nullable=False)
    status=Column(Boolean,default=False)

