class Solution:
    def search(self,nums:[int], target:int) -> int:
        left = 0;
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            num = nums[mid]

            if num == target:
                return mid

            if num > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    print(search([4,8,15,23,24,73,152,3424,6634],73))