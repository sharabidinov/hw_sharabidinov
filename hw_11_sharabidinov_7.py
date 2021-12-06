# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNum:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2
        self.complx = complex(num_1, num_2)

    def __str__(self):
        return f'{self.num_1} + {self.num_2}i'

    def __add__(self, other):
        return ComplexNum((self.complx.real + other.complx.real), (self.complx.imag + other.complx.imag))

    def __mul__(self, other):
        add_mul = self.complx.real * other.complx.real + self.complx.imag * other.complx.imag
        minus_mul = self.complx.real * other.complx.real - self.complx.imag * other.complx.imag
        return ComplexNum(add_mul, minus_mul)


if __name__ == '__main__':
    example_1 = ComplexNum(11, 7)
    example_2 = ComplexNum(7, 8)
    print(example_1 + example_2)
    print(example_1 * example_2)
