import requests
import json

res = requests.get(
    url="https://api.huaban.com/search/file",
    params={
        "text": "美女",
        "sort":"all",
        "limit": 40,
        "page": 1,
        "position": "search_pin",
        "fields": "pins:PIN,total,facets,split_words,relations"
    }
)

data_dict = json.loads(res.text)
pin_list = data_dict["pins"]
for item in pin_list:
    print(item['user']['username'], item['raw_text'])