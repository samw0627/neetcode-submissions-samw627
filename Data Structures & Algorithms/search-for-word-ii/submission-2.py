class TrieNode:
    def __init__(self):
        self.neighbours = {}
        self.word = False
        self.refs = 0 #Tracks how many words use this node
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        current = self.root
        current.refs += 1  # Increment at root
        for c in word:
            if c not in current.neighbours:
                current.neighbours[c] = TrieNode()
            current = current.neighbours[c]
            current.refs += 1  # Increment at root
        current.word = True
    def remove(self,word):
        current = self.root
        current.refs -= 1
        for char in word:
            current = current.neighbours[char]
            current.refs -= 1
    
class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #Build a trie out of the set of words
        prefix = Trie()
        for word in words:
            prefix.add(word)
        
        ROW = len(board)
        COL = len(board[0])
        visited = set()
        final = set()

        def dfs(r,c,trieNode,currentWord):
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visited or board[r][c] not in trieNode.neighbours:
                return
            visited.add((r,c))
            currentWord.append(board[r][c])
            trieNode = trieNode.neighbours[board[r][c]]
            #Check if the current character is the end of a word
            if trieNode.word:
                #add word to final list
                s = "".join(currentWord)
                final.add(s)
                trieNode.word = False # Set the word flag to false to prevent duplicates
                prefix.remove(s)
            
            dfs(r+1,c,trieNode,currentWord)
            dfs(r-1,c,trieNode,currentWord)
            dfs(r,c+1,trieNode,currentWord)
            dfs(r,c-1,trieNode,currentWord)

            #Backtracking
            currentWord.pop()
            visited.remove((r,c))
            
        #Traverse Each Node in the Trie and find it on the board
        for r in range(ROW):
            for c in range(COL):
                dfs(r,c,prefix.root,[])
        
        return list(final)
        

        