class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        '''if (len(candyType)//2)<=len(set(candyType)):
            return len(candyType)//2
        else:
            return len(set(candyType))'''
        return min(len(set(candyType)),len(candyType)//2)


        