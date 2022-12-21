import xkcd


import requests


class XkcdGatherer:
    def __init__(self):
        self.emote = '🧑‍🔬'
        self.trigger_regex = 'xkcd'

    def get(self):
        return xkcd.getRandomComic().getImageLink()
        
if __name__ == "__main__":
    test_gatherer = XkcdGatherer()
    print(test_gatherer.get())
