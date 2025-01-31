import pytest
from brewery_api_client import BreweryApiClient

@pytest.fixture(scope="session")
def base_url():
    return "https://api.openbrewerydb.org/v1"

@pytest.fixture(scope="session")
def brewery_client(base_url):
    return BreweryApiClient(base_url=base_url)