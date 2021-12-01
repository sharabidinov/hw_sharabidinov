# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    def draw(self):
        return f'Отрисовка ручкой запущена: {self.title.upper()}'


class Pencil(Stationery):
    def draw(self):
        return f'Отрисовка карнадашом запущена: {self.title.upper()}'


class Handle(Stationery):
    def draw(self):
        return f'Отрисовака маркером начата: {self.title.upper()}'


if __name__ == '__main__':
    example = Handle('marker')
    print(example.draw())
    print(example.title)