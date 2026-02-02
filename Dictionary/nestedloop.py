Samsung = {
    "Electronics": {
        "Mobile Phones": ["Galaxy S21", "Galaxy Note 20", "Galaxy Z Fold 3"],
        "Televisions": ["QLED Q90T", "Crystal UHD TU8000", "The Frame"],
        "Laptops": ["Galaxy Book Pro", "Galaxy Book Flex", "Notebook 9"]
    },
}

print(Samsung)
print("-------------------")
print(Samsung["Electronics"]["Mobile Phones"])
print("-------------------")


# Lets try looping

for x,obj in Samsung.items():
    print(f"Category: {x}")
    for y, items in obj.items():
        print(f"  Sub-category: {y}")
        for item in items:
            print(f"    Item: {item}")