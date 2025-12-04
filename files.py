import json

data = {
    "name": "Umar",
    "age": 23,
    "skills": ["Python", "Javascript"]
}

with open("user_details.json", "w") as file:
    json.dump(data, file, indent=4)


with open("user_details.json", "r") as file:
    loaded_file = json.load(file)

print(loaded_file)
