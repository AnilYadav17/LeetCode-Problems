class Solution(object):
    def findDisappearedNumbers(self, nums):
        result=[]
        s =set(nums)
        i=1
        while i<=len(nums):
            if i not in s:
                result.append(i)
            i+=1
        return result
