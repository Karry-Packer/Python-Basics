car = {
    "brand": "Tata Motors",
    "model": "Nexon",
    "year": 2020,
}
print(car)
model = car["model"]
print(f"Model: {model}")

# Can be done using get() as well
model = car.get("model")
print(f"Model using get(): {model}")

# Get keys
keys = car.keys()
print(f"Keys: {keys}")

# Adding new key-value pair
car["color"] = "Red"
print(f"Updated Car: {car}")

# Get values
values = car.values()
print(f"Values: {values}")

# Get items
items = car.items()
print(f"Items: {items}")

# Check if key exists
if "year" in car:
    print("Year key exists in the car dictionary.")


