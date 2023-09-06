# lib/dog.py

from .models import Dog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the SQLAlchemy engine
engine = create_engine('sqlite:///dogs.db')

# Create a session factory
Session = sessionmaker(bind=engine)

# Function to create a new dog record
def create(name, breed, age=None):
    session = Session()
    dog = Dog(name=name, breed=breed, age=age)
    session.add(dog)
    session.commit()
    session.close()

# Function to retrieve all dogs
def get_all():
    session = Session()
    dogs = session.query(Dog).all()
    session.close()
    return dogs

# Function to retrieve a dog by its ID
def get_by_id(id):
    session = Session()
    dog = session.query(Dog).filter_by(id=id).first()
    session.close()
    return dog

# Function to update a dog's information
def update(id, name, breed, age=None):
    session = Session()
    dog = session.query(Dog).filter_by(id=id).first()
    if dog:
        dog.name = name
        dog.breed = breed
        dog.age = age
        session.commit()
    session.close()

# Function to delete a dog by its ID
def delete(id):
    session = Session()
    dog = session.query(Dog).filter_by(id=id).first()
    if dog:
        session.delete(dog)
        session.commit()
    session.close()
