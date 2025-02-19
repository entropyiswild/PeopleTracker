# data_manager.py
import json

def save_person(name, age):
    """Save a person's name and age to people.txt."""
    with open('people.txt', 'a') as file:
        file.write(f"Name: {name}, Age: {age}\n")

def read_people():
    """Read all entries from people.txt and return them as a list of dictionaries."""
    people = []
    try:
        with open('people.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    name_part = line.split(", Age:")[0].replace("Name: ", "")
                    age_part = line.split(", Age:")[1]
                    people.append({"name": name_part, "age": int(age_part)})
    except FileNotFoundError:
        return []  # Return empty list if file doesn’t exist yet
    return people

def delete_person(name):
    """Delete a person by name from people.txt."""
    people = read_people()
    updated_people = [p for p in people if p["name"].lower() != name.lower()]
    with open('people.txt', 'w') as file:
        for person in updated_people:
            file.write(f"Name: {person['name']}, Age: {person['age']}\n")

def save_to_json(people):
    """Save people data to a JSON file."""
    with open('people.json', 'w') as file:
        json.dump(people, file, indent=4)

def read_from_json():
    """Read people data from a JSON file."""
    try:
        with open('people.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []