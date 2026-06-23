class Solution(object):
    def singleNumber(self, nums):
        for i in nums:
            if nums.count(i)!=3 and i!=1:
                return i
            elif i==1 and nums.count(i)==1:
                return 1
        