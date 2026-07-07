import json

student = {
    "name": "Khushneet",
    "age": 20,
    "course": "BCA"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")