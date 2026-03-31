class UnionFind:
    def __init__(self,n):
        self.paren = {}
        self.rank = {}

        for i in range(1,n+1):
            self.paren[i] = i
            self.rank[i] = 0
    
    def find(self,n):
        if n != self.paren[n]:
            self.paren[n] = self.find(self.paren[n]) #Path compression
        return self.paren[n]
    
    def union (self,s1,s2):
        s1_paren = self.find(s1)
        s2_paren = self.find(s2)

        if s1_paren == s2_paren:
            return False

        if self.rank[s1_paren] > self.rank[s2_paren]:
            self.paren[s2_paren] = s1_paren
        elif self.rank[s1_paren] < self.rank[s2_paren]:
            self.paren[s1_paren] = s2_paren
        else:
            self.paren[s1_paren] = s2_paren
            self.rank[s2_paren] += 1  #Update the rank of the parent   

        return True

class Solution:
     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for e in edges:
            if not union_find.union(e[0],e[1]):
                return [e[0],e[1]]

            








        

        
        
        