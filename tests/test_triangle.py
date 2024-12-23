import math

from src.Triangle import Triangle
import pytest


def test_triangle_area_positive_with_fixture(create_triangle):
    side_a, side_b, side_c = create_triangle
    t = Triangle(side_a, side_b, side_c)
    assert t.area == math.sqrt(
        ((side_a + side_b + side_c) / 2)
        * (((side_a + side_b + side_c) / 2) - side_a)
        * (((side_a + side_b + side_c) / 2) - side_b)
        * (((side_a + side_b + side_c) / 2) - side_c)
    ), f"Triangle area with {side_a}, {side_b} and {side_c} must be {t.area}"


def test_triangle_perimeter_positive_with_fixture(create_triangle):
    side_a, side_b, side_c = create_triangle
    t = Triangle(side_a, side_b, side_c)
    assert (
        t.perimeter == side_a + side_b + side_c
    ), f"Rectangle perimeter with {side_a} and {side_b} must be {t.perimeter}"


def test_triangle_area_invalid_with_fixture(create_invalid_triangle):
    side_a, side_b, side_c = create_invalid_triangle
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_perimeter_invalid_with_fixture(create_invalid_triangle):
    side_a, side_b, side_c = create_invalid_triangle
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_triangle_area_incomplete_with_fixture(create_incomplete_triangle):
    side_a, side_b = create_incomplete_triangle
    with pytest.raises(ValueError):
        Triangle(side_a, side_b)


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [(3, 4, 5, 6), (3.5, 4.5, 5.5, 7.854885)],
    ids=["integer", "float"],
)
def test_triangle_area_positive(side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == math.sqrt(
        ((side_a + side_b + side_c) / 2)
        * (((side_a + side_b + side_c) / 2) - side_a)
        * (((side_a + side_b + side_c) / 2) - side_b)
        * (((side_a + side_b + side_c) / 2) - side_c)
    ), f"Triangle area with {side_a}, {side_b} and {side_c} must be {t.area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "perimeter"),
    [(3, 4, 5, 12), (3.5, 4.5, 5.5, 13.5)],
    ids=["integer", "float"],
)
def test_triangle_perimeter_positive(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert (
        t.perimeter == side_a + side_b + side_c
    ), f"Triangle perimeter with {side_a}, {side_b} and {side_c} must be {t.perimeter}"


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [(-1, 4, 5), (3, -4, 5), (3, 4, -5), (0, 4, 5), (3, 0, 5), (3, 4, 0)],
    ids=["a<0", "b<0", "c<0", "a=0", "b=0", "c=0"],
)
def test_triangle_creation_invalid(side_a, side_b, side_c):
    with pytest.raises(
        ValueError, match="side_a, side_b and side_c must be above zero"
    ):
        Triangle(side_a, side_b, side_c)
