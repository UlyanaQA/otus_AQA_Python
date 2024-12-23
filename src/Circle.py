import math
from src.Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("radius must be above zero")
        self.radius = radius

    @property
    def area(self):
        return round(math.pi * (self.radius**2), 6)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
