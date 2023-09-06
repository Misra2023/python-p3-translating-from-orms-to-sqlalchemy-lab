# lib/models.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy engine and base
engine = create_engine('sqlite:///dogs.db')  # Use SQLite as the database
Base = declarative_base()

# Define the Dog data model
class Dog(Base):
    __tablename__ = 'dogs'  # Table name

    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String, nullable=False)   # Name column (not nullable)
    breed = Column(String, nullable=False)  # Breed column (not nullable)
    age = Column(Integer)                    # Age column (nullable)

# Create the database schema (tables)
Base.metadata.create_all(engine)
