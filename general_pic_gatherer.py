import json
import requests


class GeneralPicGatherer:
    def __init__(self, link, indexes, emote, trigger_words):
        self.link = link
        self.indexes = indexes
        self.emote = emote
        self.trigger_words = trigger_words

    def get_pic(self):
        data = requests.get(self.link).json()
        for index in self.indexes:
            data = data[index]
        return data

if __name__ == "__main__":
    fox_gatherer = GeneralPicGatherer('https://randomfox.ca/floof/', ['image'], '🦊', ['fox'])
    print(fox_gatherer.get_pic())

