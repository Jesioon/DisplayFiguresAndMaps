import requests, json
from plotly import offline

class EarthQuakes():
    """Display Earthquakes on the map with data from website"""
    def __init__(self, identificator):
        """Reading data from URL and initialize variables"""
        # Creating variables
        self.sizes, self.mags, self.longitudes, self.latitudes, self.titles = [], [], [], [], []
        # Page details and read data
        URL = f"https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/{identificator}.geojson"
        r = requests.get(URL)
        self.response = r.json()
        rediable_file = 'data/summary_all_day_earthquakes.json'
        with open(rediable_file, 'w') as f:
            json.dump(self.response, f, indent=4)

        self.features = self.response['features']

        self.attribution_variables()
        self.map_settings()

    def attribution_variables(self):
        """Attribution values for variables"""
        for feature in self.features:
            if (feature['properties']['mag'] == None or feature['geometry']['coordinates'][0] == None or
                feature['geometry']['coordinates'][1] == None or feature['properties']['title'] == None):
                continue
            else:
                self.mags.append(feature['properties']['mag'])
                self.longitudes.append(feature['geometry']['coordinates'][0])
                self.latitudes.append(feature['geometry']['coordinates'][1])
                self.titles.append(feature['properties']['title'])

            if feature['properties']['mag'] >= 0:
                self.sizes.append(5*feature['properties']['mag'])
            else:
                self.sizes.append(0.1)

    def map_settings(self):
        """Map settings"""
        self.data = [{
            'type': 'scattergeo',
            'lon': self.longitudes,
            'lat': self.latitudes,
            'opacity': 1,
            'hovertext': self.titles,
            'marker': {
                'size': self.sizes,
                'color': self.mags,
                'colorscale': 'Viridis',
                'reversescale': True,
                'colorbar': {'title': "Siła"},
            },
        }]
        self.my_layout = {
            'title': {
                'text': self.response['metadata']['title'],
                'font': {
                    'family': 'Times New Roman',
                    'size': 25,
                },
                'x': 0.5
            }
        }

        self.display()

    def display(self):
        """Display map"""
        fig = {'data': self.data, 'layout': self.my_layout}
        offline.plot(fig, filename='data/earthquakes_map.html')
