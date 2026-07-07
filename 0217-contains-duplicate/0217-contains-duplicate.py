class Solution(object):
    def containsDuplicate(self, nums):
        i=0
        result = False
        while len(nums)>i:
            if nums.count(nums[i])>1:
                result =  True
                break
            i+=1
        return result
