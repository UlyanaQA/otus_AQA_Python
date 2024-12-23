import pytest


@pytest.mark.parametrize(
    "figure_type",
    [
        "square+triangle",
        "square+circle",
        "rectangle+circle",
        "rectangle+triangle",
        "circle+triangle",
        "similar_figures",
    ],
)
def test_add_area(figure_data, figure_type):
    figure_1, figure_2, expected_sum = figure_data(figure_type)
    assert figure_1.add_area(figure_2) == pytest.approx(expected_sum, rel=1e-6)
