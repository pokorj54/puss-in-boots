import json
import requests
import random
import my_secret_token


def get_pic():
    data = requests.get('https://api.thecatapi.com/v1/images/search?&api_key={}'.format(my_secret_token.get_cat_API_token()))
    pic_url = data.json()[0]['url']
    return pic_url

if __name__ == "__main__":
   print(get_pic())

