class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels
    def move(self):
        message = f"{self.brand} Move Using its {self.wheels} Wheels!!!"
        print(message)