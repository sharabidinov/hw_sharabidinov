import sys


def sales_data(num):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{num}\n')


sales_data(sys.argv[1])
