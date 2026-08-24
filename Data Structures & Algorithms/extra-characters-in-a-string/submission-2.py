class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word = True
    def find(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.word
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        dp[-1] = 0
        trie = Trie()
        for d in dictionary:
            trie.add(d)

        for i in range(n-1,-1,-1):
            skip = 1 + dp[i+1]
            use = float('inf')
            for j in range(i+1,n+1):
                if trie.find(s[i:j]):
                    #Take the minimum
                    use = min(use,dp[j])
            dp[i] = min(skip,use)
        return dp[0]

        


        

        

        
        


        

        
        