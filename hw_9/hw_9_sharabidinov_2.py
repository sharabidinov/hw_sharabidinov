#  2. Реализовать класс Road (дорога). Определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв. метра дороги, толщиной в 1 см * число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т


class Road:
    def __init__(self, length, width, asphalt_mass, asphalt_thickness):
        self._length = length
        self._width = width
        self._asphalt_mass = asphalt_mass
        self._asphalt_thickness = asphalt_thickness

    def total_expense(self):
        result = self._length * self._width * self._asphalt_mass * self._asphalt_thickness
        return f'{self._length}м * {self._width}м * {self._asphalt_mass}кг * {self._asphalt_thickness}см = {result // 1000}т'


if __name__ == '__main__':
    # проверяем из примера задания '20 м*5000 м*25 кг*5 см = 12500 т'
    expense_1 = Road(20, 5000, 25, 5)
    print(expense_1.total_expense())
