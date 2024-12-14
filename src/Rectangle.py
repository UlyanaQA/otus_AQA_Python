from src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a: int, side_b: int):
        if side_a <= 0 or side_b <= 0:
            raise ValueError("side_a and side_b must be above zero")
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return 2 * (self.side_a + self.side_b)


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)
