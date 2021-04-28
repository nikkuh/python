class ZeroDivisionWarning(Exception):
    text = 'На этот раз прощаю, но больше так не делай!'


print('Давайте делить числа!')
try:
    top = int(input('Введите делимое: '))
    bottom = int(input('Введите делитель: '))
    if bottom == 0:
        raise ZeroDivisionWarning(ZeroDivisionWarning.text)
    print(f'Результат: {top / bottom}')
except ValueError:
    print('Это же не числа! Так ничего не получится.')
except ZeroDivisionWarning as er:
    print(er)
