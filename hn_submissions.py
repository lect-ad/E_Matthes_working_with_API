import requests
from operator import itemgetter
from plotly import offline


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")
list_of_topstories_ids = r.json()

top_articles = []
titles, title_links, comments = [], [], []
for art_id in list_of_topstories_ids[:10]:
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
    titles.append(article['title'])
    title_links.append(f"<a href='{article['hn_link']}'>"
                       f"{article['title'][:26]}</a>")
    comments.append(article['comments'])

data = [
    {
        'type': 'bar',
        'x': title_links,
        'y': comments,
        'marker': {
                    'color': comments,
                    'colorscale': 'Bluered',
                    'colorbar': {'title': 'Comments'},
                    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
                    },
        'text': titles,
        'opacity': 0.7
     }
    ]
my_layout = {
                'title': f"The Most Discussed Articles on Hacker-News",
                'titlefont': {'size': 26},
                'xaxis': {
                            'title': 'Article',
                            'titlefont': {'size': 22},
                            'tickfont': {'size': 12}
                            },
                'yaxis': {
                            'title': 'Comments',
                            'titlefont': {'size': 22},
                            'tickfont': {'size': 12}
                            }
            }
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'top_discussed_articles.html')