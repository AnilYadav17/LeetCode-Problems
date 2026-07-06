class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        count=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sub=[]
                for k in range(i,j+1):
                    sub.append(arr[k])
                if len(sub)%2!=0:
                    count+=sum(sub)


        return count