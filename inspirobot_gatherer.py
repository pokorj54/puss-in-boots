import requests

class InspirobotGatherer:
    def __init__(self):
        self.emote = '🤖'
        self.trigger_regex = 'inspir'

    def get(self, match):
        api = "http://inspirobot.me/api?generate=true"
        return requests.get(api).text
        
if __name__ == "__main__":
    test_gatherer = InspirobotGatherer()
    print(test_gatherer.get())
