class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        print(self.quantity)
        return ''

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print('Результатом вычитания должно быть положительное число.')

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity // other.quantity)

    def make_order(self, length):
        k = 0
        for _ in range(self.quantity):
            k += 1
            if k % length:
                print('*', end='')
            else:
                print('*', end='\n')


c1 = Cell(55)
c2 = Cell(15)

c2 - c1
c3 = c2 - c1 / c2
print(c3)
c3.make_order(8)
