from typing import List

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = {
                "post": [],
                "follow": []
            }

        # Store (time, tweetId)
        self.tweets[userId]["post"].insert(0, (self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.tweets:
            return []

        output = []

        # Own tweets
        for tweet in self.tweets[userId]["post"]:
            output.append(tweet)

        # Followed users' tweets
        for followeeId in self.tweets[userId]["follow"]:
            if followeeId in self.tweets:
                output.extend(self.tweets[followeeId]["post"])

        # Newest tweet first
        output.sort(reverse=True)

        # Only tweetId, maximum 10 tweets
        return [tweetId for time, tweetId in output[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.tweets:
            self.tweets[followerId] = {
                "post": [],
                "follow": []
            }

        if followeeId not in self.tweets[followerId]["follow"]:
            self.tweets[followerId]["follow"].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.tweets:
            if followeeId in self.tweets[followerId]["follow"]:
                self.tweets[followerId]["follow"].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()

obj.postTweet(2,5)
obj.follow(1,2)
obj.follow(1,2)
obj.getNewsFeed(1)

