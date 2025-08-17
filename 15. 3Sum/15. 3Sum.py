#first solution:
class Solution(object):
    def threeSum(self, nums):
        #sort list
        nums.sort()
        #create sol list
        solution = []
        #main loop
        for i in range(0, len(nums) - 2):
            fixed_number = nums[i]
            left, right = i+1 , len(nums) - 1
            while left < right:
                if fixed_number + nums[left] + nums[right] == 0:
                    if not [fixed_number, nums[left], nums[right]] in solution:
                        solution.append([fixed_number, nums[left], nums[right]])
                    right -= 1
                    left += 1
                elif fixed_number + nums[left] + nums[right] > 0:
                    right -= 1
                elif fixed_number + nums[left] + nums[right] < 0:
                    left += 1
        return solution

        

#Optimized solution:
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i ,a  in enumerate(nums):
            if i>0  and a==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total=a+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return res