class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res=[]
        for num in arr:
            if num!=0:
                res.append(num)
            else:
                res.append(0)
                res.append(0)
                
        
        for i in range(len(arr)):
            arr[i]=res[i]

        