import json

# read the HTML template
with open("animals_template.html", "r") as file:
    template = file.read()

# Load the animal Data
with open("animals_data.json", "r") as file:
    animals_data = json.load(file)

output = ""
for animal in animals_data:
    name_animal = animal.get("name", "N/A")
    characteristics_animal = animal.get("characteristics", {})
    diet_animal = characteristics_animal.get("diet", "N/A")
    type_animal = characteristics_animal.get("type", "N/A")
    location_animal = animal.get("locations", "N/A")
    locations = ", ".join(location_animal)

    output += f"Name: {name_animal}\n"
    output += f"Diet: {diet_animal}\n"
    output += f"Location: {locations}\n"
    output += f"Type: {type_animal}\n\n"

final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as file:
    file.write(final_html)