import reddit_common

reddit = reddit_common.open_reddit()

MAX_TRIES = 10

class RedditGatherer:
    def __init__(self, subreddit, emote, trigger_regex):
        self.subreddit = subreddit
        self.emote = emote
        self.trigger_regex = trigger_regex

    def get(self, match):
        subreddit = reddit.subreddit(self.subreddit)
        gallery = []
        i = 0
        while len(gallery) == 0:
            post =  subreddit.random()
            try:
                if post.is_gallery:
                    for i in post.media_metadata.items():
                        url = i[1]['p'][0]['u']
                        url = url.split("?")[0].replace("preview", "i")
                        gallery.append(url)
            except:
                i += 1
                if i == MAX_TRIES: 
                    return f"Tried to find post {MAX_TRIES} and found no suitable post."
                continue # post does not have to have this tag -> not gallery or single photo
            break
        if len(gallery) == 0:
            return post.url
        return gallery

if __name__ == "__main__":
    test_gatherer = RedditGatherer(input(), '', '')
    print(test_gatherer.get_pic())

