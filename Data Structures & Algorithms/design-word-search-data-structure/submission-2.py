class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        #Add the word into the trie
        curr = self.root
        for w in word:
            if w not in curr.children:
                #Create a new Node
                newNode = TrieNode()
                curr.children[w] = newNode
            curr = curr.children[w]
        curr.word = True
        

    def search(self, word: str) -> bool:
        #If the current char is ., then run dfs to find all branches
        root = self.root
        def dfs(index,curr):
            #Base Case: We reached the end of the word and the curr Node is the word
            if index == len(word):
                return curr.word
            char = word[index]
            if char == '.':
                #Explore all children
                for c in curr.children:
                    if dfs(index+1,curr.children[c]):
                        return True
                return False
            elif char in curr.children:
                return dfs(index+1,curr.children[char])
            return False
        return dfs(0,root)
            

        
