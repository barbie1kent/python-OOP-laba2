class Car:
    color = None
    fuel = None
    wheel_size = None
    max_speed = None

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def output(self, car):
        print(f'color: {car.color}'
              f'fuel: {car.fuel}'
              f'while_size: {car.wheel_size}'
              f'max_speed: {car.max_speed}')

myCar = Car()

myCar.color = 'red'
myCar.fuel = 50
myCar.wheel_size = '17'
myCar.max_speed = '200'