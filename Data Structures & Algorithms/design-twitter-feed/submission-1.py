class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.userPost = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userPost[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #Fetch all related posts and heapify it to maxHeap
        heap = []
        res = []
         #User can follow itself
        self.followMap[userId].add(userId)
        print(self.followMap[userId])
        for followeeId in self.followMap[userId]:
            if followeeId in self.userPost:
                #Get the most recent post for that user
                index = len(self.userPost[followeeId]) - 1
                time, tweetId = self.userPost[followeeId][index]
                heapq.heappush_max(heap,[time, tweetId, followeeId, index-1])
        
        while heap and len(res) < 10:
            time, tweetId, followeeId, nextIndex = heapq.heappop_max(heap)
            res.append(tweetId)
            if nextIndex >= 0:
                time, tweetId = self.userPost[followeeId][nextIndex]
                heapq.heappush_max(heap,[time, tweetId, followeeId, nextIndex-1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)



        
        
        
