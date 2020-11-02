import requests
import plotly.graph_objs import Bar
import plotly import offline


URL = "https://api.github.com/search/repositories?q=language:python&sort=star"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(URL, headers=headers)
response_dict = r.json()

response_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in response_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars
}]

my_layout = {'title': 'Python projects with the highest number of stars on GitHub',
             'xaxis': {'title': 'Repository'},
             'yaxis': {'title': 'Amount of stars'},
             }


