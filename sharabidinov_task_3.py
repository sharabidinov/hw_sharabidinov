user_input = int(input('введите число от 1 до 100: '))

if user_input == 1:
    print(f'{user_input} процент')
elif 1 < user_input < 5:
    print(f'{user_input} процента')
elif 5 < user_input <= 100:
    print(f'{user_input} процентов')
else:
    print('error')