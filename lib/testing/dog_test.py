# tests/test_dog.py

from lib.dog import create, get_all, get_by_id, update, delete

def test_create_and_get():
    # Create a new dog
    create("Fido", "Labrador", 5)

    # Check if the dog was created and can be retrieved
    dog = get_by_id(1)
    assert dog.name == "Fido"
    assert dog.breed == "Labrador"
    assert dog.age == 5

def test_get_all():
    # Create a few dogs
    create("Buddy", "Golden Retriever", 4)
    create("Rex", "German Shepherd", 3)

    # Get all dogs
    dogs = get_all()

    # Check if the count is correct
    assert len(dogs) == 2

def test_update():
    # Create a new dog
    create("Daisy", "Beagle", 2)

    # Update the dog's information
    update(1, "Daisy", "Bulldog", 3)

    # Check if the dog's information is updated
    dog = get_by_id(1)
    assert dog.breed == "Bulldog"
    assert dog.age == 3

def test_delete():
    # Create a new dog
    create("Luna", "Husky", 1)

    # Delete the dog
    delete(1)

    # Try to retrieve the deleted dog
    dog = get_by_id(1)
    assert dog is None
