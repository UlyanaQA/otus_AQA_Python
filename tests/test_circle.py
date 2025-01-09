import math

from src.Circle import Circle
import pytest


def test_circle_area_positive_with_fixture(create_circle):
    radius = create_circle
    c = Circle(radius)
    assert (
        c.area == math.pi * radius * radius
    ), f"Circle area with radius {radius} must be {c.area}"


def test_circle_perimeter_positive_with_fixture(create_circle):
    radius = create_circle
    c = Circle(radius)
    assert (
        c.perimeter == 2 * math.pi * radius
    ), f"Circle perimeter with radius {radius} must be {c.perimeter}"


def test_circle_area_invalid_with_fixture(create_invalid_circle):
    radius = create_invalid_circle
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_perimeter_invalid_with_fixture(create_invalid_circle):
    radius = create_invalid_circle
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize(
    ("radius", "area"),
    [(3, 28.274334), (3.5, 38.48451)],
    ids=["integer", "float"],
)
def test_circle_area_positive(radius, area):
    c = Circle(radius)
    assert (
        c.area == math.pi * radius * radius
    ), f"Circle area with radius {radius} must be {c.area}"


@pytest.mark.parametrize(
    ("radius", "perimeter"),
    [(3, 18.84956), (3.5, 21.99115)],
    ids=["integer", "float"],
)
def test_circle_perimeter_positive(radius, perimeter):
    c = Circle(radius)
    assert (
        c.perimeter == 2 * math.pi * radius
    ), f"Circle perimeter with radius {radius} must be {c.perimeter}"


@pytest.mark.parametrize(
    "radius",
    [-1, 0],
    ids=["radius<0", "radius=0"],
)
def test_circle_creation_invalid(radius):
    with pytest.raises(ValueError, match="radius must be above zero"):
        Circle(radius)
