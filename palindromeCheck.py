lst = [1,2,3,2,1]
def is_palindrome(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True 
print("The list is a palindrome." if is_palindrome(lst) else "The list is not a palindrome.")