class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        minDiff=float('inf')
        result=[]

        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff<=minDiff:
                minDiff=diff
        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff==minDiff:
                result.append([arr[i],arr[i+1]])

        return result


        return arr
        