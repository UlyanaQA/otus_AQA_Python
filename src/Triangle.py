from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, *sides: int | float):
        if len(sides) != 3:
            raise ValueError("Triangle requires exactly three sides")

        side_a, side_b, side_c = sides

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("side_a, side_b and side_c must be above zero")

        if not (
            side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a
        ):
            raise ValueError("The given sides do not form a triangle")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        half_area = (self.side_a + self.side_b + self.side_c) / 2
        return round(
            (
                half_area
                * (half_area - self.side_a)
                * (half_area - self.side_b)
                * (half_area - self.side_c)
            )
            ** 0.5,
            6,
        )

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
