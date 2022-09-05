import json
import requests
import random


def get_fact():
    data = requests.get('https://cat-fact.herokuapp.com/facts')
    js_data = data.json()
    index = random.randint(0, len(js_data)-1)
    fact = js_data[index]['text']
    return fact

if __name__ == "__main__":
   print(get_fact())
