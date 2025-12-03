# ===== LISTS =====

# Read
events = ["Breakfast", "Meeting", "Lunch"]
for event in events:
    print(event)

# Add
events.append("Brunch")

for event in events:
    print(event)

# Update
events[1] = "Dinner"
for event in events:
    print(event)

# Delete
events.remove("Breakfast")
for event in events:
    print(event)

# ===== Dictionaries =====

user = {
    "name": "Alex",
    "role": "Admin"
}

user["is_available"] = False
print(user)

user.pop("is_available")

# SETS

id_numbers = {101, 102, 101}
print(id_numbers)

# Tuples
coordinates = (10, 20)
print(coordinates[0])

coordinates[0] = 15
