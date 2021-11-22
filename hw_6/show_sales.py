import sys


def read_all():
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        print(f.read())


def read_from_end(num):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        while int(num) < len(line) + 1:
            print(line[int(num) - 1])
            num = int(num) + 1


def read_from_before(num_1, num_2):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        line = f.readlines()
        while int(num_1) < int(num_2) + 1:
            print(line[int(num_1) - 1])
            num_1 = int(num_1) + 1


'''Тут конструкция if __name__ == \'__main__\' используется как костыль, чтобы программу можно было запустить через 
терминал, и я в курсе о недостатках данной реализации. Конечно же можно было решить данный способ без создания 
функции, но я захотел реализвать это с помощью фунции '''
if __name__ == '__main__':
    if len(sys.argv) == 1:
        read_all()
    elif len(sys.argv) == 2:
        read_from_end(sys.argv[1])
    elif len(sys.argv) == 3:
        read_from_before(num_1=sys.argv[1], num_2=sys.argv[2])
