class Cell:
    def __init__(self, param):
        self.param = param
        self.symbol = '*'

    def __str__(self):
        return str(f'Количество ячеек - {self.param}')

    def __sub__(self, other):
        return Cell(abs(self.param - other.param))

    def __mul__(self, other):
        return Cell(self.param * other.param)

    def __truediv__(self, other):
        return Cell(self.param // other.param)

    def __add__(self, other):
        return Cell(abs(self.param + other.param))

    def make_order(self, count):
        x = self.param
        while x > 0:
            for k in range(1, count + 1):
                print(self.symbol, end='')
                x -= 1
                if x <= 0:
                    break
            print('\n', end='')


if __name__ == '__main__':
    a = Cell(5)
    b = Cell(10)
    c = Cell(3)
    d = Cell(2)

    print(a + b)
    print(a - b)
    print(a * b)
    print(c / d)

    a.make_order(3)
    b.make_order(3)
