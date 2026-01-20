lst = [2,3,3,5,6,7,1,1,8,8]
def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

unique_lst = unique_elements(lst)
print("Unique elements in the list:", unique_lst)