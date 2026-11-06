from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine=create_engine("sqlite:///./task_manager.db")

LocalSession=sessionmaker(bind=engine,autoflush=True)
