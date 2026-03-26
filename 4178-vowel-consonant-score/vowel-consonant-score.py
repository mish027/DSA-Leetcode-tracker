class Solution:
    def vowelConsonantScore(self, s: str) -> int:

        vowels =['a','e','i','o','u']
        
        countV=0
        countS=0
        for ch in s:

            if ch.isalpha():
                if ch in vowels:
                    countV+=1
                else:
                    countS+=1
        
        if countS>0:
            score = countV//countS
        else:
            score = 0
        return score
                

        