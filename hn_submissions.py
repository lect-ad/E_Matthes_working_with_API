import requests
from operator import itemgetter


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
list_of_topstories_ids = r.json()

top_articles = []
for art_id in list_of_topstories_ids[:50]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{art_id}.json'
    r = requests.get(url)
    print(f"Status code: {r.status_code}")
    response_dict = r.json()

    try:
        article_dict = {
                        'title': response_dict['title'],
                        'hn_link': f"https://news.ycombinator.com/item?id={art_id}",
                        'comments': response_dict['descendants']
                        }
    except KeyError:
        print(f"Couldn't get info on article with id {art_id}")
    else:
        top_articles.append(article_dict)

top_articles = sorted(top_articles, key=itemgetter('comments'), reverse=True)

for article in top_articles:
    print(f"\nTitle: {article['title']}")
    print(f"Link: {article['hn_link']}")
    print(f"Comments: {article['comments']}")