import praw
import my_secret_token
import random

reddit_credentials=my_secret_token.get_reddit_credentials()

reddit = praw.Reddit(
    client_id=reddit_credentials[0],
    client_secret=reddit_credentials[1],
    user_agent="Puss in boots by u/Cenislav",
)

class UniversalRedditGatherer:
    def __init__(self):
        self.emote = '🤖'
        self.trigger_regex = "r\/\w+"

    def get(self, match):
        subreddit = reddit.subreddit(match[2:])
        return subreddit.random().url

if __name__ == "__main__":
    test_gatherer = UniversalRedditGatherer(input(), '', '')
    print(test_gatherer.get_pic())

