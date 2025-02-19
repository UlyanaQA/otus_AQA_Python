import requests

class BreweryApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get_all_breweries(self, params=None):
        return self.session.get(f"{self.base_url}/breweries", params=params)

    def get_brewery_by_id(self, brewery_id):
        return self.session.get(f"{self.base_url}/breweries/{brewery_id}")

    def search_breweries(self, query):
        return self.session.get(f"{self.base_url}/breweries/search?query={query}")

    def get_breweries_by_type(self, brewery_type):
        return self.session.get(f"{self.base_url}/breweries?by_type={brewery_type}")

    def get_random_brewery(self):
        return self.session.get(f"{self.base_url}/breweries/random")