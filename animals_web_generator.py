import json

def load_data(file_path):
    """Loads a JSON file and returns it as a dictionary."""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

print(animals_data)

def animals_information():
    for animal in animals_data:
        name_animal = animal.get("name", "N/A")
        characteristics_animal = animal.get("characteristics", {})
        diet_animal = characteristics_animal.get("diet", "N/A")
        type_animal = characteristics_animal.get("type", "N/A")
        location_animal = animal.get("locations", "N/A")
        locations = ", ".join(location_animal)

        print(f"Name: {name_animal}")
        print(f"Diet: {diet_animal}")
        print(f"Location: {locations}")
        print(f"Type: {type_animal}")
        print()

animals_information()