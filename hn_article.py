import requests
import json


url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
content = r.json()

with open('readable_hn.json', 'w') as f:
    json.dump(content, f, indent=4)