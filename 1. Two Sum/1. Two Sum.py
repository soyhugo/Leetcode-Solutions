class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        for i,num in enumerate(nums):
            complementary = target - num
            if complementary in dictionary:
                return[dictionary[complementary], i]
            dictionary[num] = i
        return []