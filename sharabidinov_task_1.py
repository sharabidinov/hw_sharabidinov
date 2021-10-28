duration_input = int(input('duration: '))
DURATION = duration_input

days = duration_input // 3600 // 24
duration_input -= days * 3600 * 24
hours = duration_input // 3600
duration_input -= hours * 3600
minutes = duration_input // 60
duration_input -= hours * 60

if duration_input >= 86400:
    print(f'{days} дня {hours} час {minutes} мин {duration_input} сек')
elif 86400 > duration_input >= 3600:
    print(f'{hours} час {minutes} мин {duration_input} сек')
elif 3600 > duration_input >= 60:
    print(f'{minutes} мин {duration_input} сек')
elif duration_input < 60:
    print(f'{duration_input} сек')
else:
    print('ошибка')
