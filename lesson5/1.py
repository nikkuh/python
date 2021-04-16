print('Для прекращения ввода, нажмите Enter после пустой строки.')
with open('input text file.txt', 'a', encoding='utf-8') as file:
    while True:
        content = input('Введите строку для записи в файл: ')
        if content:
            print(content, file=file)
        else:
            break
