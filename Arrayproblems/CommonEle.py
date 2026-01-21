lst1= [2,3,3,5]
lst2 = [3,5,6,7]
def common_elements(lst1, lst2):
    common_lst = []
    for item in lst1:
        if item in lst2 and item not in common_lst:
            common_lst.append(item)
    return common_lst   


common_lst = common_elements(lst1, lst2)
print("Common elements in the lists:", common_lst)