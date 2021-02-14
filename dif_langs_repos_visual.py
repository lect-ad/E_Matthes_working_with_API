import requests
from plotly import offline


language = 'C++'
url = f'https://api.github.com/search/' \
      f'repositories?q=language:{language.lower()}&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repos: {response_dict['total_count']}")

list_of_repo_dicts = response_dict['items']

repos_links, repos_stars, tooltips = [], [], []
for repo in list_of_repo_dicts:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repos_links.append(f"<a href='{repo_url}'>{repo_name}</a>")

    repos_stars.append(repo['stargazers_count'])

    owner = repo['owner']['login']
    description = repo['description']
    tooltips.append(f"{owner}<br />{description}")

data = [
    {
        'type': 'bar',
        'x': repos_links,
        'y': repos_stars,
        'marker': {
                    'color': 'rgb(123, 94, 146)',
                    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
                    },
        'text': tooltips,
        'opacity': 0.7
     }
    ]
my_layout = {
                'title': f"Top Starred {language} Repos on Github",
                'titlefont': {'size': 26},
                'xaxis': {
                            'title': 'Repository',
                            'titlefont': {'size': 22},
                            'tickfont': {'size': 12}
                            },
                'yaxis': {
                            'title': 'Stars',
                            'titlefont': {'size': 22},
                            'tickfont': {'size': 12}
                            }
            }
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=f'top_{language}_repos.html')