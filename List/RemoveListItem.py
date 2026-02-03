TataCars = ["Nexon", "Altroz", "Harrier", "Safari"]
TataCars.remove("Harrier")
print(TataCars)

# If there are duplicate items, only the first occurrence is removed
TataCars.insert(2,"Nexon")
print(TataCars) 

TataCars.remove("Nexon")
print(TataCars)

# Removes @specified index using pop() method
removed_car = TataCars.pop(1)
print(f"Removed Car: {removed_car}")    
print(TataCars)

# If no index is specified, the last item is removed
last_car = TataCars.pop()
print(f"Last Removed Car: {last_car}")
print(TataCars) 

# Using del keyword to remove item at specific index
del TataCars[0]
print(TataCars) 
# Using del keyword to remove entire list
del TataCars    
