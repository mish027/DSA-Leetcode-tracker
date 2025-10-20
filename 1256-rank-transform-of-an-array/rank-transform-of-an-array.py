class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        new_arr=sorted(arr)
        hashMap={}
        i=1
        for num in new_arr:
            if num in hashMap:
                continue  
            hashMap[num]=i
            i+=1
        

        res=[]
        for num in arr:
            if num in hashMap:
                res.append(hashMap[num])
        return res
        


        
        