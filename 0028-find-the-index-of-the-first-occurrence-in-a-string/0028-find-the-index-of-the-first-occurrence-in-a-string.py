class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            match = True
            
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break

            if match:
                return(i)
                break
        else:
            return(-1)