class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders=[]
        self.times=times
        count={}
        leader=None  
        for p in persons:
            count[p]=count.get(p,0)+1
            if leader is None or count[p]>=count[leader]:
                leader=p
            self.leaders.append(leader)
        
        

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times,t)-1
        return self.leaders[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)