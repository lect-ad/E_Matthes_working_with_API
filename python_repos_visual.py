import requests
from plotly.graph_objs import Bar
from plotly import offline


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repos: {response_dict['total_count']}")

list_of_repo_dicts = response_dict['items']

repos_names, repos_stars = [], []
for repo in list_of_repo_dicts:
    repos_names.append(repo['name'])
    repos_stars.append(repo['stargazers_count'])

data = [
    {
        'type': 'bar',
        'x': repos_names,
        'y': repos_stars
     }
    ]
my_layout = {
                'title': "Top Starred Python Repos on Github",
                'xaxis': {'title': 'Repository'},
                'yaxis': {'title': 'Stars'}
            }
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='top_python_repos.html')