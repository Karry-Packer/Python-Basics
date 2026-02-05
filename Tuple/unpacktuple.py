cars = ("Toyota", "Honda", "Ford", "BMW")

# Unpacking the tuple into individual variables
car1, car2, car3, car4 = cars   
print(f"Car 1: {car1}")
print(f"Car 2: {car2}") 
print(f"Car 3: {car3}")
print(f"Car 4: {car4}")

# If you want to unpack only some of the values, you can use the * operator to ignore the rest
car1, *other_cars = cars    
print(f"Car 1: {car1}")
print(f"Other Cars: {other_cars}")

# You can also use the * operator to unpack the values into a list
*car_list, last_car = cars
print(f"Car List: {car_list}")
print(f"Last Car: {last_car}")


