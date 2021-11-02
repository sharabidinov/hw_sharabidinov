price_list = [123, 34.5, 53, 678.3, 36, 60.05, 38, 98, 48.7]

for item in price_list:
    print(f"{item:.0f} руб {item * 100 % 100:02.0f} коп")

    print('выводим цены по возрастанию')
price_list.sort()

for item in price_list:
    print(f"{item:.0f} руб {item * 100 % 100:02.0f} коп")

print('Выводим цены по убыванию')
price_list.reverse()

for item in price_list:
    print(f"{item:.0f} руб {item * 100 % 100:02.0f} коп")

# в методичке не указано как выводить, я решил вывести по убыванию
print('выводим цены пяти самых дорогих товаров')
index = 0
while index < 5:
    print(f"{price_list[index]:.0f} руб {price_list[index] * 100 % 100:02.0f} коп")
    index += 1
