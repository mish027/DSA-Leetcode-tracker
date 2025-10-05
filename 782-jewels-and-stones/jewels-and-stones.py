class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count=0
        jewelsSet=set(jewels)  
        for stone in stones:
            if stone in jewelsSet:
                count+=1
        return count

    '''Time Complexity:
    - Creating the set jewelsSet from the list jewels takes O(J) time, where J is the number of jewels.
    - Iterating through the list stones takes O(S) time, where S is the number of stones.
    - Checking if a stone is in jewelsSet is an O(1) operation due to the hash set.
    - Overall, the total time complexity is O(J + S).

    Space Complexity:
    - The set jewelsSet requires O(J) space to store the jewels.
    - The other variables use constant space.
    - Overall, the space complexity is O(J).
    '''