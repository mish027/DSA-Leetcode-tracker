class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res=[]
        res.append(first)
        for i in range(len(encoded)):
            res.append(encoded[i]^res[i])
        return res

        