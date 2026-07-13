class Solution(object):
    def reverseWords(self, s):
        s = s.split()
        result=[]
        for i in s:
            result.append(i[::-1])
        
        return " ".join(result)