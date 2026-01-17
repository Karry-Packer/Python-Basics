list1 = [1,2,3,4,5,6,7,8,9,10]
reversed_list = []
for i in range(len(list1)-1, -1, -1):
    reversed_list.append(list1[i])
print("Original List:", list1)
print("Reversed List:", reversed_list)