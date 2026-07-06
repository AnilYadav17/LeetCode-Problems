class Solution(object):
    def sortedSquares(self, nums):
        return sorted(map(lambda x:x**2 ,nums))
       