class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        nums=[]
        XOR=0
        for i in range(n):
            nums.append(start+2*i)
            XOR^=nums[i]
        return XOR