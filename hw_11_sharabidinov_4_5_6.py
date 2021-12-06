# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class HardwareStore:
    def __init__(self, model, price, amount):
        self.model = model
        self.price = price
        self.amount = amount
        self.current_product_lst = []
        self.final_product_lst = []
        self.data_base = {'Модель': self.model, 'Цена': self.price, 'Количество': self.amount}

    def __str__(self):
        return f'Модель: {self.model} \nЦена: {self.price} \nКоличество: {self.amount}'

    def product_accept(self):
        try:
            product = input('Введите наименование товара: ')
            product_price = int(input('Введите цену товара '))
            product_amount = int(input('Введите количество товара '))
            product_data = {'Модель': product, 'Цена': product_price, 'Количество': product_amount}
            self.data_base.update(product_data)
            self.current_product_lst.append(self.current_product_lst)
            print(f'Текущий список: {self.data_base}')
        except:
            return 'Неправильно введены данные'

        user_input = input('Для выхода введите Quit, для продолжения Enter')
        if user_input.title() == 'Quit':
            self.final_product_lst.append(self.current_product_lst)
            print(f'Полный список товаров: {self.final_product_lst}')
            return 'Выход осуществлен'
        elif user_input.title() == 'Enter':
            return HardwareStore.product_accept(self)


class Printer(HardwareStore):
    def parameter_1(self):
        return 'уникальный параметр Printer'


class Scanner(HardwareStore):
    def parameter_2(self):
        return 'уникальный параметр Scaner'


class Xerox(HardwareStore):
    def parameter_3(self):
        return 'уникальный параметр Xerox'


if __name__ == '__main__':
    printer = Printer('Samsung Xpress M2020', 45600, 2)
    scanner = Scanner('Canon imageFORMULA R40 Office Document Scanner', 35000, 4)
    xerox = Xerox('Brother Monochrome Laser Printer', 30000, 2)
    print(printer)
    print(printer.parameter_1())
    print('-' * 50)
    print(scanner)
    print(scanner.parameter_2())
    print('-' * 50)
    print(xerox)
    print(xerox.parameter_3())
