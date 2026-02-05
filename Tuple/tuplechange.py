Cars = ("Toyota", "Honda", "Ford", "BMW")
print(f"Original Cars Tuple: {Cars}")

car_list = list(Cars)
car_list[1] = "Hyundai"
Cars = tuple(car_list)
print(f"Modified Cars Tuple: {Cars}")   

# Lets try to add a new car to the tuple
car_list.append("Audi")
Cars = tuple(car_list)  
print(f"Extended Cars Tuple: {Cars}")

# if you ever want to add new values to a tuple, you can concatenate it with another tuple
new_cars = ("Mercedes", "Tesla")
Cars = Cars + new_cars
print(f"Concatenated Cars Tuple: {Cars}")   

# if you want to remove a car from the tuple, you can convert it to a list, remove the item, and convert it back to a tuple
car_list.remove("Ford")
Cars = tuple(car_list)
print(f"Cars Tuple after removing 'Ford': {Cars}")
