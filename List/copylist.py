Cars = ['Indica', 'Nano', 'Safari', 'Harrier', 'Tiago', 'Tigor', 'Altroz', 'Nexon']
		
list_cars = Cars.copy()
print(f"Original Cars List: {Cars}")
print(f"Copied Cars List: {list_cars}")

# using list() function

a_list  = list(Cars)
print(f"a_list using list() function: {a_list}")

# using slicing
b_list = Cars[:]
print(f"b_list using slicing: {b_list}")
