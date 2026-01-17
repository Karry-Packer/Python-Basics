# # /In this we will count how many times an element appears in a list.

# lst = [1, 3, 4, 5, 1, 2, 1, 3, 4]
# def count_element(lst, element):
#     count = 0
#     for item in lst:
#         if item == element:
#             count += 1
#     return count
# print("The element 1 appears", count_element(lst, 1), "times in the list.")
# print("The element 4 appears", count_element(lst,4), "times in the list.")

# print("The element 3 appears", lst.count(3), "times in the list.")
# most_common_element = max(lst, key=lst.count)
# least_common_element = min(lst, key=lst.count)
# print(f"Element {most_common_element} appears Most", lst.count(most_common_element), "times in the list.")
# print("Element{least_common_element} appears Least", lst.count(min(lst, key=lst.count)), "times in the list.")




lst = [1,2,2,5,5,4]
n = len(lst)
for i in range(n):
    count = 1
    for j in range(i + 1, n):
        if lst[i] == lst[j]:
            count += 1
    # To avoid duplicate prints, check if this element has appeared before
    if lst[i] not in lst[:i]:
        print("The element", lst[i], "appears", count, "times in the list.")
