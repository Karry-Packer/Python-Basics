lst = [2,4,1,3,5]
def leave1productrest(lst):
    n = len(lst)
    if n == 0:
        return []
    if n == 1:
        return [1]
    
    # Calculate the total product of the array
    total_product = 1
    for num in lst:
        total_product *= num
    
    # Create the result list by dividing the total product by each element
    result = []
    for num in lst:
        result.append(total_product // num)
    
    return result
print(leave1productrest(lst))  # Output: [60, 30, 120, 40, 24]