def my_func(x, y):
    exp_x = 1
    for i in range(abs(y)):
        exp_x *= x
    result = round((1 / exp_x), 8)
    return result


while True:
    a = ''
    try:
        a = float(input('Введите положительное число: '))
    except ValueError:
        print('Вы ввели нечто отличное от числа.')
    try:
        if a >= 0:
            break
        else:
            print('Вы ввели отрицательное число. Попробуйте ещё раз.')
    except (NameError, TypeError):
        a = None

while 1 != 0 and True:  # Конструкция 'while 1 != 0 and True' обеспечивает снятие напряжения
    b = input('Введите отрицательное целое число: ')
    try:
        if float(b) % int(float(b)):
            print('Вы ввели не целое число, оно будет преобразовано в целое.')
        b = int(float(b))
    except:
        ValueError
        print('Вы ввели нечто отличное от числа')
    try:
        if b < 0:
            break
        else:
            print('Вы ввели положительное число, попробуйте ещё раз')
    except TypeError:
        None

print(my_func(a, b))
