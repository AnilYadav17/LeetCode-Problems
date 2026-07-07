class Solution(object):
    def moveZeroes(self, nums):
        with_zero = []
        without_zero = []
        for i in nums:
            if i!=0:
                without_zero.append(i)
            else:
                with_zero.append(i)
        
        new = without_zero + with_zero
        for i in range(len(nums)):
            nums[i] = new[i]
        
        