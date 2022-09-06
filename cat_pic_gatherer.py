import json
import requests
import my_secret_token


class CatPicGatherer:
    def __init__(self):
        self.emote = '🐈'
        self.trigger_words = ['cat', 'kitty', 'puss']

    def get_pic(self):
        data = requests.get('https://api.thecatapi.com/v1/images/search?&api_key={}'.format(my_secret_token.get_cat_API_token()))
        pic_url = data.json()[0]['url']
        return pic_url

if __name__ == "__main__":
    test_gatherer = CatPicGatherer()
    print(test_gatherer.get_pic())

