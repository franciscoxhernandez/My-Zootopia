import json

# read the HTML template
with open("animals_template.html", "r", encoding="utf-8") as file:
    template = file.read()

# Load the animal Data
with open("animals_data.json", "r") as file:
    animals_data = json.load(file)

def serialize_animals(animals_data):
    output = "" # define an empty string
    for animal in animals_data:
        name_animal = animal.get("name", "N/A")
        characteristics_animal = animal.get("characteristics", {})
        diet_animal = characteristics_animal.get("diet", "N/A")
        type_animal = characteristics_animal.get("type", "N/A")
        location_animal = animal.get("locations", "N/A")
        locations = ", ".join(location_animal)

        output += '<li class="cards__item">\n'
        output += f'    <div class="card__title">{name_animal}</div>\n'
        output += '         <div class="card__text">\n'
        output += '             <ul class="card__list">\n'
        output += f'                <li class="card__list-item"><strong>Diet:</strong> {diet_animal}</li>\n'
        output += f'                <li class="card__list-item"><strong>Location:</strong> {locations}</li>\n'
        output += f'                <li class="card__list-item"><strong>Type:</strong> {type_animal}</li>\n'
        output += '             </ul>\n'
        output += '         </div>\n'
        output += '     </li>\n'
    return output

output = serialize_animals(animals_data)
final_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as file:
    file.write(final_html)
