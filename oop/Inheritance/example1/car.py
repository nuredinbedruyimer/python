from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, brand, wheels, ac):
        super().__init__(brand, wheels)
        self.ac = ac
    def play_music(self):
        print(f"{self.brand} is Playing Music!!")