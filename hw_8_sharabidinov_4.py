from functools import wraps


def value_checker(check):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in args:
                if check(i):
                    return func(*args, **kwargs)
                else:
                    raise ValueError(f'invalid value {i}')

        return wrapper

    return decorator


@value_checker(lambda x: x > 0)
def calc_cube(x: int):
    return x ** 3


print(calc_cube(4))
print(calc_cube.__name__)
print(calc_cube(-3))
