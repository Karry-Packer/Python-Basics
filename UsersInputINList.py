# We wil ask the user to input 5 numbers and store them in a list.print the list
input_numbers = []
num_elements = int(input("How many numbers do you want to enter? "))
for i in range(num_elements):
    num = input(f"Enter value {i+1}: ")
    try:
        num = int(num)
    except ValueError:
        pass
    input_numbers.append(num)
print("The numbers you entered are:", input_numbers)

# Now replacing the third number with 100
input_numbers[2]= 100
print("After replacing the third number with 100, the list is:", input_numbers)
# Output:       

for i in input_numbers:
    print