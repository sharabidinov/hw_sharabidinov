from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        lst = [el for el in (*args, *kwargs.values())]
        for item in lst:
            print(f'{func.__name__}({item}: {type(item)})')
        return func(*args, **kwargs)

    return wrapper


@type_logger
def sums(z):
    return z + 2


@type_logger
def calc_cube(x, c):
    return x ** 3 + c


sums(2)
calc_cube(2.8, 4)
# print(sums(4))
# print(calc_cube(5.5, 4)) вернет результат функцмм
