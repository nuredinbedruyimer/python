class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector(x, y)
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Vector(x, y)
        
    def __str__(self):
        return f"{self.x, self.y}"



point1 = Vector(2, 3)
point2 = Vector(10, 9)

print(point1 + point2)
print(point1 - point2)
print(point1 * point2)
print(point1 / point2)



