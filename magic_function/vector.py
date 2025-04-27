import math


class Vector:
    """ Class to Implement Vector class which consist of all vector related opration"""
    def __init__(self, x, y):
        """ Intialize all field of the Vector class with its cordinate values(x, y)"""
        self.x = x
        self.y = y
    def __add__(self, other):
        """ Adding Vectors """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        """ Subtracting Vectors """

        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __mul__(self, other):
        """ Multiplying Vectors """

        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)
    def __truediv__(self, other):
        """ Dividing Vectors """

        x = self.x / other.x
        y = self.y / other.y
        return Vector(x, y)
        
    def __str__(self):
        """ Making The obect Human readable"""
        return f"{self.x, self.y}"
    def magnitude(self):
        """ Finding The magnitude Using  M = sqrt(x^2 + y^2)"""
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __lt__(self, other):
        return self.magnitude() < other.magnitude()
    def __le__(self, other):
        return self.magnitude() <= other.magnitude()
    def _gt__(self, other):
        return self.magnitude() > other.magnitude()
    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()
    def __eq__(self, other):
        return self.magnitude() == other.magnitude()
    
        
    



point1 = Vector(2, 3)
point2 = Vector(10, 9)
point3 = Vector(10, 9)


print(point1 + point2)
print(point1 - point2)
print(point1 * point2)
print(point1 / point2)
print((point1 - point2).magnitude())

print(point3 == point2)




