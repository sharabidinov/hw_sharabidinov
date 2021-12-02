from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def tissue_consumption(self):
        pass

    def __add__(self, other):
        return self.tissue_consumption + other.tissue_consumption


class Coat(Clothes):
    @property
    def tissue_consumption(self):
        result = self.size / 6.5 + 0.5
        return result


class Costume(Clothes):
    @property
    def tissue_consumption(self):
        result = (self.size * 2 + 0.3) / 100  # ковертируем в см в м
        return result


if __name__ == '__main__':
    coat = Coat(58)
    costume = Costume(240)
    total = coat + costume
    print(f'{total:.2f}')
