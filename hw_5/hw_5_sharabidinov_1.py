def generator(el: int):
    for digit in range(1, el + 1, 2):
        yield digit


odd_num = generator(30)

print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
print(next(odd_num))
