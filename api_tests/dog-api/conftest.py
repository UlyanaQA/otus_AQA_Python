import pytest
from dog_api_client import DogApiClient

@pytest.fixture(scope="session")
def base_url():
    return "https://dog.ceo/api"

@pytest.fixture(scope="session")
def dog_client(base_url):
    return DogApiClient(base_url=base_url)