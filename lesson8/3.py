import re


class IsNotDigit(Exception):
    text = 'Это не число.'


li = []
while True:
    try:
        n = input('Введите число: ')
        if n == 'stop':
            break
        elif re.match('^-?\d+\.?\d*$', n):
            li.append(float(n))
        else:
            raise IsNotDigit(IsNotDigit.text)
    except IsNotDigit as err:
        print(err)

print(li)
