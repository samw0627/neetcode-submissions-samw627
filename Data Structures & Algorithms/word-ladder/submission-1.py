class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #Build Adj List
        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)
        
        visited = set()
        q = deque()
        q.append(beginWord)
        visited.add(beginWord)
        level = 1
        while q:
            for p in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return level

                for i in range(len(word)):
                    #Process the pattern before adding all unvisitied node to list
                    pattern = word[:i] + "*" + word[i+1:]
                    for neigh in adj[pattern]:
                        if neigh not in visited:
                            visited.add(neigh)
                            q.append(neigh)

            level += 1
        return 0

        
    #hot -> pot, lot
    #   -> hut, hat
    #   -> hob, hoe

        