class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        j=0
        flag=0

        if not s:
            return True

        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
                j+=1
                flag=1
            elif s[i]!=t[j]:
                j+=1
        
        if i==len(s) and flag==1:
            return True
        return False
        