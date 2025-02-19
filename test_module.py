import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="URL для проверки статус кода"
    )
    parser.addoption(
        "--status_code",
        action="store",
        type=int,
        default=200,
        help="Ожидаемый HTTP статус код"
    )

@pytest.fixture
def target_url(request):
    return request.config.getoption("--url")

@pytest.fixture
def expected_status(request):
    return request.config.getoption("--status_code")

def test_url_status_code(target_url, expected_status):
    response = requests.get(target_url, timeout=5)
    assert response.status_code == expected_status, (
        f"Ожидался статус {expected_status}, но получен {response.status_code}"
    )
