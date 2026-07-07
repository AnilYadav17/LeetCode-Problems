class Solution(object):
    def plusOne(self, digits):
        s = ""
        for i in digits:
            s+=str(i)

        ans = int(s)+1

        result=[]
        for i in str(ans):
            result.append(int(i))

        return result