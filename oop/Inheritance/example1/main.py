from vehicle import Vehicle
from car import Car


random_car = Vehicle("BYW", 4)
random_bike = Vehicle("Bike1", 2)

random_car.move()
random_bike.move()

byw = Car("BYW", 4, True)

byw.play_music()