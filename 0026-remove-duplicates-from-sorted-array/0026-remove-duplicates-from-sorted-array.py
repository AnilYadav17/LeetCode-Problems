class Solution(object):
    def removeDuplicates(self, nums):

        result = []

        for i in nums:
            if i not in result:
                result.append(i)

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)