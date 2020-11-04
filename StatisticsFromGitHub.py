import requests
from plotly import offline

class GitHubCharts():
    """Class is responsible for drawing a Bar graph with datas about languages from GitHub"""

    def __init__(self, language):
        """Reading datas from URL and initialize variables"""
        #Creating variables
        self.repo_links, self.stars, self.labels = [], [], []
        self.language = language
        #Page details and read datas
        URL = f"https://api.github.com/search/repositories?q=language:{self.language}&sort=star"
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(URL, headers=headers)
        response_dict = r.json()

        response_dicts = response_dict['items']

        self.my_language_settings()
        self.write_datas(response_dicts)

    def my_language_settings(self):
        """Subtitle settings for Bar graph title"""
        if self.language == 'cpp':
            self.language = 'C++'
        elif self.language == 'javascript':
            self.language = 'JavaScript'
        elif self.language == 'php' or self.language == 'sql':
            self.language = self.language.upper()
        else:
            self.language = self.language.title()

    def write_datas(self, response_dicts):
        """Write datas from page to variables"""
        for repo_dict in response_dicts:
            repo_name = repo_dict['name']
            repo_url = repo_dict['html_url']
            self.repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
            self.stars.append(repo_dict['stargazers_count'])
            owner = repo_dict['owner']['login']
            description = repo_dict['description']
            self.labels.append(f"{owner}<br />{description}")

        self.bar_settings()

    def bar_settings(self):
        """Bar graph settings"""
        data = [{
        'type': 'bar',
        'x': self.repo_links,
        'y': self.stars,
        'hovertext': self.labels,
        'marker': {
            'color': '#4682B4',
            'line': {'width': 1.5, 'color': '#778899'},
        'opacity': 0.8,
        },
        }]


        my_layout = {'title': {
                    'text': f"{self.language} projects with the highest number of stars on GitHub.\n"
                            f" You can press on project name to go to the project page",
                    'font': {
                        'family': 'Times New Roman',
                        'size': 25
                        },
                    'x': 0.5,
                    },

                    'xaxis': {
                        'title': 'Repository',
                        'titlefont': {'size': 25},
                        'tickfont': {'size': 15},
                        },
                    'yaxis': {
                        'title': 'Amount of stars',
                        'titlefont': {'size': 25},
                        'tickfont': {'size': 15},
                        },
                    }

        self.draw(data, my_layout)

    def draw(self, data, my_layout):
        """Drawing Bar graph"""
        fig = {'data': data, "layout": my_layout}
        offline.plot(fig, filename=f"data/{self.language.lower()}_GitHub.html")

