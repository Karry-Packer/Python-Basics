TataCars = ["Nexon", "Altroz", "Harrier", "Safari"]

for car in TataCars:
    print(f"Car: {car}")

for index in range(len(TataCars)):
    print(f"Index: {index}, Car: {TataCars[index]}") 


# using while loop

index = 0
while index < len(TataCars):
    print(f"Index: {index}, Car: {TataCars[index]}")
    index += 1  

# looping  through list comprehension

[print(f"Car {car}") for car in TataCars]


# using enumerate to get index and value
for index, car in enumerate(TataCars):
    print(f"Index: {index}, Car: {car}")    
    