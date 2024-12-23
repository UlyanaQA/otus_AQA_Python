from src.Rectangle import Rectangle
import pytest


def test_rectangle_area_positive_with_fixture(create_rectangle):
    side_a, side_b = create_rectangle
    r = Rectangle(side_a, side_b)
    assert (
        r.area == side_a * side_b
    ), f"Rectangle area with {side_a} and {side_b} must be {r.area}"


def test_rectangle_perimeter_positive_with_fixture(create_rectangle):
    side_a, side_b = create_rectangle
    r = Rectangle(side_a, side_b)
    assert r.perimeter == 2 * (
        side_a + side_b
    ), f"Rectangle perimeter with {side_a} and {side_b} must be {r.perimeter}"


def test_rectangle_area_invalid_with_fixture(create_invalid_rectangle):
    side_a, side_b = create_invalid_rectangle
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_rectangle_perimeter_invalid_with_fixture(create_invalid_rectangle):
    side_a, side_b = create_invalid_rectangle
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [(3, 5, 15), (3.5, 5.5, 19.25)],
    ids=["integer", "float"],
)
def test_rectangle_area_positive(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert (
        r.area == side_a * side_b
    ), f"Rectangle area with {side_a} and {side_b} must be {r.area}"


@pytest.mark.parametrize(
    ("side_a", "side_b", "perimeter"),
    [(3, 5, 16), (3.5, 5.5, 18)],
    ids=["integer", "float"],
)
def test_rectangle_perimeter_positive(side_a, side_b, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.perimeter == 2 * (
        side_a + side_b
    ), f"Rectangle perimeter with {side_a} and {side_b} must be {r.perimeter}"


@pytest.mark.parametrize(
    "side_a, side_b",
    [(-1, 4), (3, -1), (0, 4), (4, 0)],
    ids=["a<0", "b<0", "a=0", "b=0"],
)
def test_rectangle_creation_invalid(side_a, side_b):
    with pytest.raises(ValueError, match="side_a and side_b must be above zero"):
        Rectangle(side_a, side_b)
