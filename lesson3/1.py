def division(div1, div2):
    try:
        return round(div1 / div2, 4)
    except ZeroDivisionError as error:
        print(error)


print(division(int(input('Введите делимое: ')), int(input('Введите делитель: '))))
