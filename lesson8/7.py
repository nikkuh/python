import re

"""Конструктор класса будет принимать только строковые значения формата 'x +/- yi', где x и y > 0."""
class Complex:

    def __init__(self, complex_number):
        if re.match('^\d+\s.\s\d+[i]$', complex_number):
            self.complex_number = complex_number
        else:
            print('!Wrong format!')

    def make_list(self):
        num_list = []
        num_list.append(float(self.complex_number.split()[0]))
        if self.complex_number.split()[1] == '-':
            num_list.append(float(f'-{self.complex_number.split()[-1][:-1]}'))
        else:
            num_list.append(float(f'{self.complex_number.split()[-1][:-1]}'))
        return num_list

    def __mul__(self, other):
        x1, y1 = self.make_list()
        x2, y2 = other.make_list()
        raw_list = [round(x1 * x2 - y1 * y2), round(x1 * x2 + y1 * y2)]
        sign = '+' if raw_list[1] > 0 else '-'
        result = f'{raw_list[0]} {sign} {abs(raw_list[1])}i'
        return result

    def __add__(self, other):
        x1, y1 = self.make_list()
        x2, y2 = other.make_list()
        raw_list = [round(x1 + x2), round(y1 + y2)]
        sign = '+' if raw_list[1] > 0 else '-'
        result = f'{raw_list[0]} {sign} {abs(raw_list[1])}i'
        return result


a1 = Complex('2 - 15i')
b1 = Complex('2 + 2i')
c1 = Complex('5+ 3i')
d1 = Complex('-7-3i')
print(a1 + b1)
print(a1 * b1)
