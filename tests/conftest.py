import pytest

from Circle import Circle
from Rectangle import Square, Rectangle
from Triangle import Triangle


@pytest.fixture(scope="session")
def create_rectangle():
    a = 3
    b = 5
    a += 1
    b += 1

    yield a, b
    a -= 1
    b -= 1


@pytest.fixture(scope="session")
def create_invalid_rectangle():
    a = 0
    b = -5

    return a, b


@pytest.fixture(scope="session")
def create_square():
    a = 4
    return a


@pytest.fixture(scope="session")
def create_invalid_square():
    a = -4
    return a


@pytest.fixture(scope="session")
def create_circle():
    r = 6
    return r


@pytest.fixture(scope="session")
def create_invalid_circle():
    r = -6
    return r


@pytest.fixture(scope="session")
def create_triangle():
    a = 3
    b = 4
    c = 5
    return a, b, c


@pytest.fixture(scope="session")
def create_invalid_triangle():
    a = -3
    b = 4
    c = 5
    return a, b, c


@pytest.fixture(scope="session")
def create_incomplete_triangle():
    a = -3
    b = 4
    return a, b


@pytest.fixture()
def figure_data():
    def _wrapper(figure_type: str):
        figures = {
            "square+triangle": (Square(10), Triangle(3, 4, 5), 106),
            "square+circle": (
                Square(10),
                Circle(3),
                round(128.274334, 6),
            ),  # Округляем ожидаемую сумму
            "rectangle+circle": (Rectangle(3, 5), Circle(3), round(43.274334, 6)),
            "rectangle+triangle": (Rectangle(3, 5), Triangle(3, 4, 5), 21),
            "circle+triangle": (Circle(3), Triangle(3, 4, 5), round(34.274334, 6)),
            "similar_figures": (Rectangle(3, 5), Rectangle(3, 5), 30),
        }
        return figures.get(figure_type)

    return _wrapper
