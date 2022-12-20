from math import pi

class InvalidCircle(Exception):
    pass

class Circle:
    def __init__(self, radius):
        self.radius = radius
        if not self.is_valid():
            raise InvalidCircle

    def circumference(self):
        return round(2 * self.radius * pi, 2)

    def area(self):
        return round(self.radius * self.radius * pi, 2)

    def is_valid(self):
        if isinstance(self.radius, (float)):
            return self.radius > 0

circle = Circle(.5)
print('Radius:', circle.radius,
      '\nCircumference:', circle.circumference(),
      '\nArea:', circle.area())