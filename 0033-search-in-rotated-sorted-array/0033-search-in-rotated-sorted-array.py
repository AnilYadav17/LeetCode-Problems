class Solution(object):
    def search(self, nums, target):
        x=0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
                x=1
        if x==0:
            return -1