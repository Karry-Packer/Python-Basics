cars = {"Ford", "BMW", "Volvo"}
numbers = {1, 2, 3}



# Joining two sets into one using union
combined = cars.union(numbers)
print("Combined Set:", combined)

# Joining sets using the set() constructor
combined_constructor = set(list(cars) + list(numbers))
print("Combined Set using constructor:", combined_constructor)

# Joining sets using unpacking
combined_unpacking = {*cars, *numbers}
print("Combined Set using unpacking:", combined_unpacking)

