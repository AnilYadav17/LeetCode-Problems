class Solution(object):
    def findUnsortedSubarray(self, nums):
        sorted_nums=sorted(nums)
        start = -1
        end = -1
        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                start=i
                break

        for i in range(len(nums)-1,-1,-1):
            if nums[i] != sorted_nums[i]:
                end=i
                break

        if start==-1 and end==-1:
            return 0
        else:
            return end-start+1