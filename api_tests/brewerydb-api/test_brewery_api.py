import pytest


def test_get_all_breweries(brewery_client):
    response = brewery_client.get_all_breweries(params={"per_page": 5})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.parametrize("brewery_type", ["micro", "nano", "regional"])
def test_get_breweries_by_type(brewery_client, brewery_type):
    response = brewery_client.get_breweries_by_type(brewery_type)
    assert response.status_code == 200
    data = response.json()
    assert all(brewery["brewery_type"] == brewery_type for brewery in data)


def test_get_brewery_by_id(brewery_client):
    # Тест с реально существующим brewery_id
    response = brewery_client.get_all_breweries(params={"per_page": 1})
    brewery_id = response.json()[0]["id"]

    response = brewery_client.get_brewery_by_id(brewery_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == brewery_id


@pytest.mark.parametrize("search_query", ["brew", "ale", "beer"])
def test_search_breweries(brewery_client, search_query):
    response = brewery_client.search_breweries(search_query)
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(search_query.lower() in brewery["name"].lower() for brewery in data)


def test_random_brewery(brewery_client):
    response = brewery_client.get_random_brewery()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1



