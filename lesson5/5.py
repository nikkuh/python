wr_content = input('Введите набор чисел, разделённых пробелами: ')
with open('text_5.txt', 'w', encoding='utf-8') as file:
    file.write(wr_content)
with open('text_5.txt', 'r', encoding='utf-8') as file:
    rd_content = map(float, file.read().split())
print(sum(rd_content))
