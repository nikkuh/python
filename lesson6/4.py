class Car:
    speed = 0
    name = None
    color = None
    direction = 'вперёд'
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self, speed):
        self.speed = speed
        print('Машина поехала.')

    def stop(self):
        self.speed = 0
        print('Машина остановилась.')

    def turn(self, direction):
        self.direction = direction
        print(f'Теперь машина едет {direction}.')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч.' if self.speed < 60 else f'Скорость {self.speed} км/ч! Вы превысили скорость!')


class WorkCar(Car):
    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч.' if self.speed < 40 else f'Скорость {self.speed} км/ч! Вы превысили скорость!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


traktor = WorkCar('Belarus', 'Синий')
traktor.go(120)
traktor.show_speed()
traktor.turn('в сторону центра')
print(traktor.is_police)

police = PoliceCar('Skoda', 'Белый')
print(police.is_police)
police.turn('на заправку')
police.go(40)
police.show_speed()
police.stop()
