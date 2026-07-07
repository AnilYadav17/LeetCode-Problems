class Solution(object):
    def moveZeroes(self, nums):
        zero=[]
        nonzero=[]
        for i in nums:
            if i==0:
                zero.append(i)
            else:
                nonzero.append(i)
        new=nonzero+zero
        for i in range(len(nums)):
            nums[i] = new[i]
        
        