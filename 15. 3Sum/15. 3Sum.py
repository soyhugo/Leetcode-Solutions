class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        n = len(nums)

        left = 0
        while left < n - 2:
            if left > 0 and nums[left] == nums[left - 1]:
                left += 1
                continue

            middle = left + 1
            right = n - 1

            while middle < right:
                current = nums[left] + nums[middle] + nums[right]

                if current == 0:
                    solution.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1

                    # FIX: skip duplicates
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current < 0:
                    middle += 1
                else:
                    right -= 1

            left += 1
        return solution