import reddit_common

reddit = reddit_common.open_reddit()

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

