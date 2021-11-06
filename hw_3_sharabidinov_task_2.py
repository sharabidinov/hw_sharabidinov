def num_translate(num: str):
    translation = {'one': 'один',
                   'two': 'два',
                   'three': 'три',
                   'four': 'четыре',
                   'five': 'четыре',
                   'six': 'шесть',
                   'seven': 'семь',
                   'eight': 'восемь',
                   'nine': 'девять',
                   'ten': 'десять',
                   'One': 'Один',
                   'Two': 'Два',
                   'Three': 'Три',
                   'Four': 'Четыре',
                   'Five': 'Пять',
                   'Six': 'Шесть',
                   'Seven': 'Семь',
                   'Eight': 'Восемь',
                   'Nine': 'Девять',
                   'Ten': 'Десять'
                   }
    if num in translation:
        return translation[num]
    return None


print(num_translate('eight'))
print(num_translate('Eight'))
print(num_translate('asdg'))