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
                   'ten': 'десять'}
    if num in translation:
        return translation[num]
    else:
        return None


print(num_translate('eight'))
print(num_translate('eigasdg'))
