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

    def get(self, match):
        subreddit = reddit.subreddit(self.subreddit)
        post =  subreddit.random()
        gallery = []
        try:
            if post.is_gallery:
                for i in post.media_metadata.items():
                    url = i[1]['p'][0]['u']
                    url = url.split("?")[0].replace("preview", "i")
                    gallery.append(url)
        except:
            pass # post does not have to have this tag
        if len(gallery) == 0:
            return post.url
        return gallery

if __name__ == "__main__":
    test_gatherer = RedditGatherer(input(), '', '')
    print(test_gatherer.get_pic())

