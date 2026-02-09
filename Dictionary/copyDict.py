car_Dict = {
    "brand": "Tata Motors",
    "model": "Nexon",   
    "year": 2020,
    "color": "Red",
}
print(f"Original Car: {car_Dict}")
# Copying the dictionary using copy() method    
copied_car = car_Dict.copy()
print(f"Copied Car: {copied_car}")
# Modifying the copied dictionary to show that original dictionary remains unchanged
copied_car["color"] = "Blue"
print(f"After modifying copied_car: {copied_car}")
print(f"Original Car after modifying copied_car: {car_Dict}")
