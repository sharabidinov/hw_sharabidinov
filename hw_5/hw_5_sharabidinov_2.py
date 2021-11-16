odd_nums_gen = (odd for odd in range(1, int(input('Введите число ')) + 1, 2)) # если ввести 7 то генератор исчерпается

print(type(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
