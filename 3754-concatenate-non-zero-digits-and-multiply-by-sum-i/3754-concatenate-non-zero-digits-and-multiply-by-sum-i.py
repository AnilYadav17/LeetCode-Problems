class Solution(object):
    def sumAndMultiply(self, n):
        if int(n)!=0:
            sum=0
            num=""
            for i in str(n):
                if int(i)!=0:
                    num+=i
                    sum+=int(i)

            return int(num)*sum
        
        else:
            return 0