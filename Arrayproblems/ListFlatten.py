lst = [1,[2,3],4,[5,6,[7,8]]]
flat_list = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flat_list.append(item)

flatten(lst)
print("Flattened List:", flat_list)