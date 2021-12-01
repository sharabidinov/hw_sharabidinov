from time import sleep

# 1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт


class TrafficLight:
    __color = 'black'

    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green

    def running(self):
        if self.red == 'red' and self.yellow == 'yellow' and self.green == 'green':
            print(self.red)
            sleep(7)
            print(self.yellow)
            sleep(2)
            print(self.green)
            sleep(7)
            print('the end')
            sleep(3)
        else:
            raise ValueError('incorrect value')


if __name__ == '__main__':
    a = TrafficLight('red', 'yellow', 'green')
    a.running()
    b = TrafficLight('d', 'yellow', 'green')
    b.running()
