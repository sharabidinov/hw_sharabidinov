from itertools import zip_longest
from sys import exit

with open('users.csv', 'r', encoding='utf-8') as f_1:
    data_1 = f_1.read().replace(',', ' ').split('\n')

with open('hobby.csv', 'r', encoding='utf-8') as f_2:
    data_2 = f_2.read().replace(',', ', ').split('\n')

data_dict = {}
data_lst = []
if len(data_1) >= len(data_2):
    for item in zip_longest(data_1, data_2):
        data_lst.append(item)
    for key, value in data_lst:
        data_dict.setdefault(key, value)
else:
    exit(1)

with open('users_data.txt', 'w', encoding='utf-8') as f_dict:
    for el in data_dict:
        f_dict.write(f'{el}: {data_dict[el]} \n')
