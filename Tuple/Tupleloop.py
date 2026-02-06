cars = ("Toyota", "Honda", "Ford", "BMW")
for car in cars:
    print(car)

# Using enumerate to get index and value
for index, car in enumerate(cars):
    print(f"Car {index + 1}: {car}")

# Using a while loop to iterate through the tuple
index = 0
while index < len(cars):
    print(cars[index])
    index += 1

# Using a for loop with range to access elements by index
for i in range(len(cars)):
    print(cars[i])

# Using tuple unpacking in a loop
for car1, car2, car3, car4 in [cars]:
    print(f"Car 1: {car1}")
    print(f"Car 2: {car2}")
    print(f"Car 3: {car3}")
    print(f"Car 4: {car4}")
