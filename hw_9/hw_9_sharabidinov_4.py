# 4. Реализуйте базовый класс Car. У класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.


class Car:
    def __init__(self, name, color, speed, direction, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.direction = direction
        self.is_police = is_police

    def go(self):
        info_start = 'Машина поехала'
        return info_start

    def stop(self):
        info_stop = 'Машина остановилась'
        return info_stop

    def turn(self):
        if self.direction == 'прямо' or self.direction == 'Прямо' or self.direction == 'ПРЯМО':
            return 'Машина поехала прямо'
        else:
            return f'Машина повернула {self.direction}'

    def show_speed(self):
        return f'{self.name} движется со скоростью {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} превысила скорость'


class SportCar(Car):
    def show_speed(self):
        return f'Спортивный автомобиль {self.name} движется со скоростью {self.speed()}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name}  превысила скорость'


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


if __name__ == '__main__':
    police_car = PoliceCar('ДПС', 'Белый', 80)
    print(police_car.go())
    print(police_car.show_speed())
    work_car = WorkCar('Гелик', 'Черный', 80, 'прямо')
    print(work_car.show_speed())
    print(work_car.stop())