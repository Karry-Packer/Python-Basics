# Using Append Method
Tata_Cars = ["Nexon", "Harrier", "Altroz"]
Tata_Cars.append("Tiago")
print(Tata_Cars)    

# using insert Method
Tata_Cars.insert(1, "Safari")
print(Tata_Cars)

# To append elements from another list using extend method
More_Tata_Cars = ["Punch", "Tigor"]
Tata_Cars.extend(More_Tata_Cars)
print(Tata_Cars)

# extend method only append list but tuple as well

More_Vehicles = ("Hexa", "Indica")
Tata_Cars.extend(More_Vehicles) 
print(Tata_Cars)

# Using + operator to add lists
Even_More_Vehicles = ["Sierra", "Zest"] 
Tata_Cars = Tata_Cars + Even_More_Vehicles
print(Tata_Cars)  

# Using *= operator to repeat list elements
Tata_Cars *= 2          
print(Tata_Cars)    

