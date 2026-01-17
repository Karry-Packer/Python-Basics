lst = [2,1,5,6,3,4]

# Square elements at even indices
for i in range(len(lst)):
    if i % 2 == 0:
        lst[i] = lst[i] ** 2

print("List after squaring elements at even indices:", lst)