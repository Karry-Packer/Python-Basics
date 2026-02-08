cars = {"Ford", "Volvo", "BMW"}
cars.remove("Volvo")  # Remove "Volvo" from the set
print(cars)  # Output: {'Ford', 'BMW'}



# Using discard() to remove an element that may not exist
cars.discard("Audi")  # This will not raise an error if "Audi" is not in the set
print(cars)  # Output: {'Ford', 'BMW'}


# Using pop() to remove an arbitrary element from the set
removed_car = cars.pop()  # Removes and returns an arbitrary element
print("Removed Car:", removed_car)  # Output: Removed Car: Ford (or BMW)
print(cars)  # Output: {'BMW'} (or {'Ford'})

# Using clear() to remove all elements from the set
cars.clear()
print(cars)  # Output: set()


# Using del to delete the entire set
del cars
# Attempting to print cars after deletion will raise an error
try:
    print(cars)
except NameError:
    print("The set 'cars' has been deleted and is no longer accessible.")
    

