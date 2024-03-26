import math


class Restaurant:
    cuisine_type = "Ethiopian"
    manager_name = "Monkey D Luffy"

    def __init__(self, name , address):
        self.name = name
        self.address = address
        
    def print_info(self):
        return "Restaurant {} Located At {}".format(self.name, self.address)
    @classmethod
    def set_cuisine_type(cls, cuisine):
        cls.cuisine_type = cuisine
    @classmethod
    def set_manager(cls, manager_name):
        cls.manager_name = manager_name
    @classmethod
    def from_string(cls, res):
        name, address = res.split("-")
        return cls(name, address)
    



r = Restaurant("Golden Gate", "Dessie")
r2 = Restaurant("Hilton ", "Addis Ababa")
print(r.cuisine_type)
print(r2.cuisine_type)        
        
Restaurant.set_cuisine_type("Whatever Whatever")
print(r.cuisine_type)
print(r2.cuisine_type)  

Restaurant.set_manager("Monkey D Luffy")

print(r.manager_name)
print(r2.manager_name) 

# restaurant_info1 = "ResturantDUBAI-Dubai"
# name, address = restaurant_info1.split("-")

 

# r3 = Restaurant(name, address)

restaurant_info1 = "ResturantDUBAI-Dubai"

r3 = Restaurant.from_string(restaurant_info1)

print(r3.print_info())
      
# static method example


import math

class Geometry:
    @staticmethod
    def calculate_circle_area(radius):
        """Calculate the area of a circle given its radius."""
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return math.pi * radius * radius

    @staticmethod
    def calculate_rectangle_area(length, width):
        """Calculate the area of a rectangle."""
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        return length * width


# Example Usage
circle_area = Geometry.calculate_circle_area(5)
print(f"Circle Area: {circle_area}")  # Output: Circle Area: 78.53981633974483

rectangle_area = Geometry.calculate_rectangle_area(4, 6)
print(f"Rectangle Area: {rectangle_area}")  # Output: Rectangle Area: 24

