class TrieNode:
    def __init__(self):
        self.neigh = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.neigh:
                curr.neigh[w] = TrieNode()
            curr = curr.neigh[w]
        curr.word = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(curr,i):
            if i == len(word):
                return curr.word
            if word[i] == ".":
                #Recursively search all neighbors
                for n in curr.neigh.values():
                    if dfs(n,i+1):
                        return True
                return False
            else:
                if word[i] in curr.neigh:
                    curr = curr.neigh[word[i]]
                    return dfs(curr,i+1)
                else:
                    return False
        
        return dfs(curr,0)


                
            
            



        
