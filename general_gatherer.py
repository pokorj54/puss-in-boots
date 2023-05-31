import json
import requests


class GeneralGatherer:
    def __init__(self, link, indexes, emote, trigger_regex):
        self.link = link
        self.indexes = indexes
        self.emote = emote
        self.trigger_regex = trigger_regex

    def get(self, match):
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

