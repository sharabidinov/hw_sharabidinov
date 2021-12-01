# 3. Реализовать базовый класс Worker. Определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income); проверить работу примера на реальных данных:
# создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'Fullname: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Total income: {sum(self._Worker__income.values())}$'


if __name__ == '__main__':
    example = Position('Alexey', 'Varashilov', 'middle java developer', 3000, 900)
    print(example.get_full_name())
    print(example.get_total_income())
    print(example.name)
    print(example.surname)
    print(sum(example._Worker__income.values()))
