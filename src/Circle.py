import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("side_a and side_b must be above zero")
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius * self.radius

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
