class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict={}

        for char in s:
            if char not in dict:
                dict[char]=0
            dict[char]+=1

        for char in s:
            if dict[char]==1:
                return s.index(char)
        return -1