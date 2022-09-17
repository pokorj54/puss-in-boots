import json
import requests


class GeneralGatherer:
    def __init__(self, link, indexes, emote, trigger_words):
        self.link = link
        self.indexes = indexes
        self.emote = emote
        self.trigger_words = trigger_words

    def get(self):
        data = requests.get(self.link)
        if self.indexes == None:
            return data
        data = data.json()
        for index in self.indexes:
            data = data[index]
        return data

if __name__ == "__main__":
    test_gatherer = GeneralGatherer('https://some-random-api.ml/img/raccoon', ['link'], '🦝', ['raccoon', 'racoon']) # Raccoon
    print(test_gatherer.get())

