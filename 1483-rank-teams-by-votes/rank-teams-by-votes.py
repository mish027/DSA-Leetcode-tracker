class Solution:
    def rankTeams(self, votes: List[str]) -> str:

        hashMap={}

        for vote in votes:
            for i,char in enumerate(vote):
                if char not in hashMap:
                    hashMap[char]=[0]*len(vote)
                hashMap[char][i]+=1
        voted_alphasort=sorted(hashMap.keys())

        return "".join(sorted(voted_alphasort, key=lambda x: hashMap[x],reverse=True))




        