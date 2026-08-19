class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_edge = {}
        in_edge = {}
    
        for i in range(1,n+1):
            in_edge[i] = []
            out_edge[i] = []

        for s,t in trust:
            out_edge[s].append(t)
            in_edge[t].append(s)
        
        for i in range(1,n+1):
            if len(out_edge[i]) == 0 and len(in_edge[i]) == n-1:
                return i
        
        return -1
        

        

        