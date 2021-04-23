from abc import abstractmethod


class Clothes:
    @abstractmethod
    def calc_material(self):
        pass


class Coat(Clothes):
    size = None

    def __init__(self, size):
        self.size = size

    @property
    def calc_material(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):
    height = None

    def __init__(self, height):
        self.height = height

    @property
    def calc_material(self):
        return round(self.height * 2 + 0.3, 2)


coat1 = Coat(50)
suit1 = Suit(1.5)
print(coat1.calc_material)
print(suit1.calc_material)
