# Problem 6 - Dictionaries & Nesting
# Store the details of persons in a dictionary and print some data from it.
# Values can be strings, numbers, lists or even other dictionaries.

persons = {
    "P1": {
        "name": "Minhazul",
        "age": 22,
        "skills": ["Python", "C#", "SQL"],
        "address": {"city": "Dhaka", "zip": "1229"},
    },
    "P2": {
        "name": "Rahim",
        "age": 21,
        "skills": ["Java", "Python"],
        "address": {"city": "Chattogram", "zip": "4000"},
    },
}

# access nested values
print("P1 name     :", persons["P1"]["name"])
print("P1 city     :", persons["P1"]["address"]["city"])
print("P2 1st skill:", persons["P2"]["skills"][0])

# add a new person and update an existing value
persons["P3"] = {
    "name": "Karim",
    "age": 23,
    "skills": ["HTML", "CSS"],
    "address": {"city": "Sylhet", "zip": "3100"},
}
persons["P2"]["age"] = 22
persons["P2"]["skills"].append("AI")

# loop over all persons
for pid, info in persons.items():
    skills = ", ".join(info["skills"])
    print(pid, "|", info["name"], "|", info["age"], "|", info["address"]["city"], "|", skills)

# useful dictionary methods
print("Keys        :", list(persons.keys()))
print("Has P4?     :", "P4" in persons)
print("get() demo  :", persons.get("P4", "not found"))
