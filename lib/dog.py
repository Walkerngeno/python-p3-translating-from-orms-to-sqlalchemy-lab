# lib/dog.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Dog

# Define the SQLite database URL
SQLITE_URL = 'sqlite:///mydatabase.db'

# Create an SQLAlchemy engine
engine = create_engine(SQLITE_URL)

# Create a session factory
Session = sessionmaker(bind=engine)

# Function to create a table for the Dog model
def create_table(Base, engine):
    Base.metadata.create_all(engine)

# Function to save a dog object to the database
def save(session, dog):
    session.add(dog)
    session.commit()

# Function to get all dogs from the database
def get_all(session):
    return session.query(Dog).all()

# Function to find a dog by name
def find_by_name(session, name):
    return session.query(Dog).filter_by(name=name).first()

# Function to find a dog by ID
def find_by_id(session, id):
    return session.query(Dog).filter_by(id=id).first()

# Function to find dogs by name and breed
def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name=name, breed=breed).first()

# Function to update a dog's breed
def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()

# Main function for testing
def main():
    Base.metadata.create_all(engine)
    session = Session()

    # Example usage:
    dog1 = Dog(name='Buddy', breed='Golden Retriever')
    save(session, dog1)

    fanny = find_by_name_and_breed(session, 'fanny', 'cockapoo')
    if fanny is not None:
        print(f"Dog Name: {fanny.name}, Breed: {fanny.breed}")
    else:
        print("Dog not found.")

    session.close()

if __name__ == '__main__':
    main()
