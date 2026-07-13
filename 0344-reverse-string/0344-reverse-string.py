class Solution(object):
    def reverseString(self, s):
        x = 0
        y = len(s)-1

        while x<y:
            s[x],s[y] = s[y],s[x]
            x+=1
            y-=1

       