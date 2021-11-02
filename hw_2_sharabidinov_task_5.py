price_list = [123, 34.5, 53, 678.3, 36, 60.05, 38, 98, 48.7]

for item in price_list:
    print(f"{item:.0f} руб {item * 100 % 100:02.0f} коп")
