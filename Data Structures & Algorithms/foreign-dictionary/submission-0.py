class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]
        charset = set()
        for word in words:
            for c in word:
                charset.add(c)
        
        adj = defaultdict(set)
        for w in range(1,len(words)):
            word1 = words[w-1]
            word2 = words[w]
            word_length = min(len(word1),len(word2))

            for i in range(word_length):
                if word1[i] != word2[i]:
                    #Establish edge on adjacency list
                    adj[word1[i]].add(word2[i])
                    break
            
            else:
                if len(word1) > len(word2):
                    return ""
                
            
            
        
        visited = set()
        path = set()
        top_sort = []

        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)

            for neigh in adj[node]:
                if not dfs(neigh):
                    return False
            path.remove(node)
            visited.add(node)
            top_sort.append(node)

            return True
        
        print(charset)

        for char in charset:
            if not dfs(char):
                return ""
        
        top_sort.reverse()
        return "".join(top_sort)



            
        #Run topological sort to get the ordering
        



        