Alist  = [56,45,21,78,12,9,34,67]
minVal = Alist[0]
print(minVal)


for  i in range(1,len(Alist)):
    if Alist[i]< minVal:
        minVal = Alist[i]

print("The lowest value in the list is: ", minVal)