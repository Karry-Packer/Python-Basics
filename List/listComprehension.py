Tata_cars = ['Indica', 'Nano', 'Safari', 'Harrier', 'Tiago', 'Tigor', 'Altroz', 'Nexon']

newlist = []

for car in Tata_cars:
    if 'a' in car:    # Here it will check only a not A so be careful
        newlist.append(car)

print(newlist)

# same thing can be done using list comprehension
# Syntax: [expression for item in iterable if condition == True]
newlist_comp = [car for car in Tata_cars if 'a' in car]
print(f"newlist_comp: {newlist_comp}")

one_more_list = [car for car in Tata_cars if car != 'Nano']
print(f"one_more_list: {one_more_list}")

last_list = [car.upper() for car in Tata_cars]
print(f"last_list: {last_list}")
