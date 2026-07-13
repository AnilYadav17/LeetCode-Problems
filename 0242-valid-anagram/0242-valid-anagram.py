class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if s.count(i)!=t.count(i):
                    return False
        return True