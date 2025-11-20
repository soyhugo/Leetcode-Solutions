class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1 

        while left <= right:
            middle = left + (right - left) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1

        return -1