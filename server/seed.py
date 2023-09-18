#!/usr/bin/env python3

from random import choice as rc

from faker import Faker


from app import app, db
from models import Owner, Pet

def seed_database():
    """Seeds the database with fake data."""

    with app.app_context():
        # Delete all existing owners and pets from the database.
        Pet.query.delete()
        Owner.query.delete()

        # Create a list of 50 owners, each with a random name.
        owners = []
        for n in range(50):
            owner = Owner(name=Faker().name())
            owners.append(owner)

        # Add all of the owners to the database.
        db.session.add_all(owners)

        # Create a list of 100 pets, each with a random name, species, and owner.
        pets = []
        species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']
        for n in range(100):
            pet = Pet(name=Faker().first_name(), species=rc(species), owner=rc(owners))
            pets.append(pet)

        # Add all of the pets to the database.
        db.session.add_all(pets)

        # Commit the changes to the database.
        db.session.commit()

if __name__ == '__main__':
    seed_database()
    
