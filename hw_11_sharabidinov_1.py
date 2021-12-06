# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата: день-месяц-год.
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    def __str__(self):
        return self.day_month_year

    @classmethod
    def str_to_int(cls, day_month_year):
        date = []

        for i in day_month_year.split('-'):
            date.append(i)
        # print(type(int(date[0])), type(int(date[1])), type(int(date[2])))
        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid_date(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 < year <= 2021:
                    return f'Валидная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'


if __name__ == '__main__':
    today = Date('11-1-2001')
    print(today)
    print(Date.valid_date(11, 11, 2022))
    print(today.valid_date(11, 13, 2011))
    print(Date.str_to_int('11-11-2011'))
    print(today.str_to_int('11-11-2020'))
    print(Date.valid_date(1, 11, 2000))
