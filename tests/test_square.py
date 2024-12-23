from src.Rectangle import Square
import pytest


def test_square_area_positive_with_fixture(create_square):
    side_a = create_square
    r = Square(side_a)
    assert r.area == side_a * side_a, f"Square area with {side_a} must be {r.area}"


def test_square_perimeter_positive_with_fixture(create_square):
    side_a = create_square
    r = Square(side_a)
    assert (
        r.perimeter == 4 * side_a
    ), f"Square perimeter with {side_a} must be {r.perimeter}"


def test_square_area_invalid_with_fixture(create_invalid_square):
    side_a = create_invalid_square
    with pytest.raises(ValueError):
        Square(side_a)


def test_square_perimeter_invalid_with_fixture(create_invalid_square):
    side_a = create_invalid_square
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize(
    ("side_a", "area"),
    [(3, 9), (3.5, 12.25)],
    ids=["integer", "float"],
)
def test_square_area_positive(side_a, area):
    r = Square(side_a)
    assert r.area == side_a * side_a, f"Square area with {side_a} must be {r.area}"


@pytest.mark.parametrize(
    ("side_a", "perimeter"),
    [(3, 12), (3.5, 14)],
    ids=["integer", "float"],
)
def test_square_perimeter_positive(side_a, perimeter):
    r = Square(side_a)
    assert (
        r.perimeter == 4 * side_a
    ), f"Square perimeter with {side_a} must be {r.perimeter}"


@pytest.mark.parametrize(
    "side_a",
    [-1, 0],
    ids=["a<0", "a=0"],
)
def test_square_creation_invalid(side_a):
    with pytest.raises(ValueError, match="side_a must be above zero"):
        Square(side_a)
