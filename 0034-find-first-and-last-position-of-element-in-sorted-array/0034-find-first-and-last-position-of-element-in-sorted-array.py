class Solution(object):
    def searchRange(self, nums, target):
        ans=[]
        start=-1
        end=-1
        if nums!=[]:
            for i in range(len(nums)):
                if nums[i] == target:
                    start=i
                    break
            for i in range(len(nums)-1,start-1,-1):
                if nums[i] == target:
                    end=i
                    break
            return [start,end]
        else:
            return [start,end]