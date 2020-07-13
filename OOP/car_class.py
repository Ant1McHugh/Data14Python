class Car:

    def __init__(self, doors, model, make, gears):
        self.doors = doors
        self.model = model
        self.make = make
        self.gears = gears
        self.__start_speed = 0
        self.__top_speed = 100

    def _set_top_speed(self, top_speed):
        self.__top_speed = top_speed

    def acceleration(self, vroom):
        self.__start_speed += int(vroom)
        if self.__start_speed == self.__top_speed:
            return "Top Speed Reached"
        if self.__start_speed > self.__top_speed:
            self.__start_speed = self.__top_speed
            return "Top Speed Reached"
        return self.__start_speed

    def braking(self, screech):
        self.__start_speed -= int(screech)
        if self.__start_speed == 0:
            return "Stationary"
        if self.__start_speed < 0:
            self.__start_speed = 0
            return "Stationary"
        return self.__start_speed

new_car = Car(4, "911", "Porsche", "Automatic")

print(new_car.acceleration(10))
print(new_car.acceleration(50))
print(new_car.braking(30))
print(new_car.braking(35))
print(new_car.acceleration(15))