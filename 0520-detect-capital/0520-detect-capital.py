class Solution(object):
    def detectCapitalUse(self, word):
        i=0
        flag=False
        count=0
        while i<len(word):
            if word[i]>='A' and word[i]<="Z":
                count+=1
            i+=1

        if count==0 or count==len(word):
            flag=True

        if count==1:
            if word[0]>='A' and word[0]<='Z':
                flag=True

        return flag