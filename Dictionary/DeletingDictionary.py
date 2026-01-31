car = {
    "brand": "Tata Motors",
    "model": "Nexon",
    "year": 2020,
    "color": "Red",
}
print(f"Original Car: {car}")

# Deleting a key-value pair

car.pop("model")
print(f"After pop('model'): {car}")

# popitem() removes the last inserted key-value pair
removed_item = car.popitem()
print(f"After popitem(): {car}, Removed Item: {removed_item}")

# Deleting using del keyword
del car["year"] 
print(f"After del car['year']: {car}")

# Clearing the entire dictionary
car.clear()
print(f"After clear(): {car}")