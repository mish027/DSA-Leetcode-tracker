class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        minDiff=float('inf')
        result=[]

        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff<minDiff:
                minDiff=diff
                result=[[arr[i],arr[i+1]]] #initialise first element as min absolute diff elements
       
            elif diff==minDiff:
                result.append([arr[i],arr[i+1]])

        return result
        