lst = [10, 20, 4, 45, 99, 99, 99]
def second_highest(lst):
    highest = second_highest = float('-inf')
    for number in lst:
        if number > highest:
            second_highest = highest
            highest = number
        elif number > second_highest and number != highest:
            second_highest = number
    return second_highest if second_highest != float('-inf') else None

result = second_highest(lst)
if result is not None:
    print("The second highest number in the list is:", result)