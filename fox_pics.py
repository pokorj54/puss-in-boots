import json
import requests
import random
import my_secret_token


def get_pic():
    data = requests.get('https://randomfox.ca/floof/')
    pic_url = data.json()['image']
    return pic_url

if __name__ == "__main__":
   print(get_pic())

