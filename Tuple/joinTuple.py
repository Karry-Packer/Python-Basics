cars = ("Hyundai", "Kia", "Mazda")

numbers = (1, 2, 3)

# Joining two tuples into one
combined = cars + numbers
print("Combined Tuple:", combined)  

# Joining tuples using the tuple() constructor
combined_constructor = tuple(list(cars) + list(numbers))
print("Combined Tuple using constructor:", combined_constructor)   

# Joining tuples using unpacking
combined_unpacking = (*cars, *numbers)
print("Combined Tuple using unpacking:", combined_unpacking)

# Multiplying a tuple to repeat its elements
repeated_cars = cars * 2
print("Repeated Cars Tuple:", repeated_cars)


