def two_sumn(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None
print(two_sumn([2, 7, 11, 15], 9))  # [0, 1]
print(two_sumn([3, 2, 4], 6))  # [1, 2]
print(two_sumn([3, 3], 6))  # [0, 1]