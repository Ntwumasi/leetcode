def isPalidrome(s):
#above i am defining a function which take a string as a input
    left = 0
    right = len(s) -1
#using the left right two pointer technique i am setting left and right
    while left < right:
        if s[left] != s[right]:
            return False
#here i am saying while the value of left is not equal to the value of right perform this logic
#and the logic is if left is not equal to right the return false
        left += 1
        right -= 1
#increment/decrement pointers
        return True
    
print(isPalidrome("racecar"))
print(isPalidrome("racecars"))