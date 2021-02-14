import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repos: {response_dict['total_count']}")

list_of_repo_dicts = response_dict['items']
print(f"Repos returned: {len(list_of_repo_dicts)}")

print(f"\nSome info about all the repos got:")
for repo in list_of_repo_dicts:
    print(f"Name: {repo['name']}")
    print(f"Owner: {repo['owner']['login']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Repository url: {repo['html_url']}")
    print(f"Created: {repo['created_at']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}\n")