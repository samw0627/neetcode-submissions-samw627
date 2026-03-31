class TrieNode:
    def __init__(self):
        self.neighbors = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.prefixRoot = TrieNode()

        
    def addWord(self, word: str) -> None:
        current = self.prefixRoot
        for c in word:
            if c not in current.neighbors:
                current.neighbors[c] = TrieNode()
            current = current.neighbors[c]
        current.word = True

    
            


    def search(self, word: str) -> bool:
        def dfs(i,node):
            #Base Case: when we reach the end of the word
            if i == len(word):
                return node.word
            if word[i] == ".":
                for n in node.neighbors.values():
                    if dfs(i+1,n):
                        return True
                return False
            else:
                if word[i] not in node.neighbors:
                    return False

                return dfs(i+1,node.neighbors[word[i]])

        return dfs(0,self.prefixRoot)





        


            
        
        
