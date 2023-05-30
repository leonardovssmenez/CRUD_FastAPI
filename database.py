from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
# Create a sqlite engine instance
engine=create_engine("postgresql://postgres:102030@localhost/item_db",
    echo=True
)
 
# Create a DeclarativeMeta instance
Base = declarative_base()
 
# Create SessionLocal class
SessionLocal = sessionmaker(bind=engine)