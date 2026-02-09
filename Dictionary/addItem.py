car_Dict = {
    "brand": "Tata Motors",
    "model": "Nexon",   
    "year": 2020,
    "color": "Red",
}

print(f"Original Car: {car_Dict}")
# Adding a new key-value pair
car_Dict["price"] = 1000000
print(f"After adding price: {car_Dict}")

# Adding multiple key-value pairs using update() method
additional_info = { "mileage": "17 km/l", "fuel_type": "Petrol"}
car_Dict.update(additional_info)    
print(f"After update with additional_info: {car_Dict}") 

# Adding a key-value pair where the key already exists will update the value
car_Dict["color"] = "Blue"
print(f"After updating color: {car_Dict}")
