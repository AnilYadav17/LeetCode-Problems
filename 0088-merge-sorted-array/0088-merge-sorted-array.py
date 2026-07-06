class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result=[]
        # for i in range(m):
        #     result.append(nums1[i])
        # for j in range(n):
        #     result.append(nums2[j])

        for i in range(m):
            result.append(nums1[i])

        for j in range(n):
            result.append(nums2[j])

        result.sort()
        
        for i in range(m + n):
            nums1[i] = result[i]
        return result