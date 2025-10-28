class Solution:
    def countKeyChanges(self, s: str) -> int:

        length=len(s)
        count=0
        for i in range(length-1):
            if s[i].lower()!=s[i+1].lower():
                count+=1
        return count

        