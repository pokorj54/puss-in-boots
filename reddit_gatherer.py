import praw
import my_secret_token
import random

reddit_credentials=my_secret_token.get_reddit_credentials()

reddit = praw.Reddit(
    client_id=reddit_credentials[0],
    client_secret=reddit_credentials[1],
    user_agent="Puss in boots by u/Cenislav",
)

class RedditGatherer:
    def __init__(self, subreddit, emote, trigger_regex):
        self.subreddit = subreddit
        self.emote = emote
        self.trigger_regex = trigger_regex

    def get(self):
        subreddit = reddit.subreddit(self.subreddit)
        return subreddit.random().url

if __name__ == "__main__":
    test_gatherer = RedditGatherer(input(), '', '')
    print(test_gatherer.get_pic())

