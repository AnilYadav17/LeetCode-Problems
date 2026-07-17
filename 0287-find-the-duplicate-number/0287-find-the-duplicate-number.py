class Solution(object):
    def findDuplicate(self, nums):
        d = dict()
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]  = 1
            else:
                return nums[i]
                break
            
        