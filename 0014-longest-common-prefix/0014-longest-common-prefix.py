class Solution(object):
    def longestCommonPrefix(self, strs):
        string=""
        f_word = strs[0]
        
        for i in range(len(f_word)):
            match=True
            for word in strs:
                if i >= len(word) or word[i] != f_word[i]:
                    match = False
                    break
            if match:
                string+=f_word[i]
            else:
                break
        return string
            