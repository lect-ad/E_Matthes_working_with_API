import requests


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url=url, headers=headers)
print(f'Status code: {r.status_code}')

response_dict = r.json()

print(f"Total repos: {response_dict['total_count']}")

list_of_repo_dicts = response_dict['items']
print(f"Repos returned: {len(list_of_repo_dicts)}")

first_repo = list_of_repo_dicts[0]
print(f"\nSome info about the 1st repo:")
print(f"Name: {first_repo['name']}")
print(f"Owner: {first_repo['owner']['login']}")
print(f"Stars: {first_repo['stargazers_count']}")
print(f"Repository url: {first_repo['html_url']}")
print(f"Created: {first_repo['created_at']}")
print(f"Updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")