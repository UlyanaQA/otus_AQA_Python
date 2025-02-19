import pytest

def test_list_all_breeds(dog_client):
    response = dog_client.get_list_all_breeds()
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert isinstance(data["message"], dict)

def test_get_random_image(dog_client):
    response = dog_client.get_single_random_image()
    assert response.status_code == 200
    data = response.json()
    assert data["message"].endswith(('.jpg', '.jpeg', '.png'))

@pytest.mark.parametrize("breed", ['shiba', 'retriever/golden', 'husky'])
def test_get_breed_images(dog_client, breed):
    response = dog_client.get_random_image_from_collection(breed)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["message"], str)


@pytest.mark.parametrize("breed, expected_subs", [
    ('hound', ['afghan', 'basset', 'blood']),
    ('retriever', ['chesapeake', 'curly', 'golden']),
    ('bulldog', ['boston', 'english', 'french']),
    ('dachshund', [])  # Согласно текущему API, нет подпород
])
def test_get_sub_breeds(dog_client, breed, expected_subs):
    response = dog_client.get_list_all_sub_breeds(breed)

    # Проверка базовой структуры ответа
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "status" in data
    assert data["status"] == "success"
    assert isinstance(data["message"], list)

    # Проверка ожидаемых подпород
    if expected_subs:
        assert all(sub in data["message"] for sub in expected_subs)
    else:
        assert data["message"] == []

def test_non_existent_breed(dog_client):
    response = dog_client.get_random_image_from_collection('non_existent_breed')
    assert response.status_code == 404
    data = response.json()
    assert data["status"] == "error"