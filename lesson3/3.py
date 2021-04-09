def my_func(a, b, c):
    """Функция возвращает сумму 2ух наибольших аргументов"""
    li = [a, b, c]
    a1 = max(li)
    li.remove(a1)
    b1 = max(li)
    return a1 + b1


print(my_func(1, 2, 3))
