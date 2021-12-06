# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
# нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class ZeroDivErr(ZeroDivisionError):
    def __init__(self, notification):
        self.notification = notification


if __name__ == '__main__':
    try:
        numeral = int(input('Введите делимое: '))
        denominator = int(input('введите знаменатель: '))
        if denominator == 0:
            raise ZeroDivErr('division by zero')
    except ZeroDivErr as err:
        print(err)
    else:
        print(numeral / denominator)