print('Введите числа разделённые пробелом. Объекты,отличные от чисел не будут обработаны.')
print('Для выхода используйте символ "q".')
total_sum = 0
exit_marker = False
while not exit_marker:
    float_list = []
    new_in = input().split()
    for n in new_in:
        if n == 'q':
            exit_marker = True
            break
        else:
            try:
                n = float(n)
            except ValueError:
                continue
            float_list.append(n)
    total_sum += sum(float_list)
    print(f'Текущая итерация = {sum(float_list)}. Общая сумма = {total_sum}.')
