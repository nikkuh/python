with open('text_4.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
new_content = []
en = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
ru = ('Ноль', 'Один', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь', 'Восемь', 'Девять')

for el in content:
    if el.split()[0] in en:
        new_content.append(f'{ru[en.index(el.split()[0])]} - {(el.split()[2])}')

print(new_content)
with open('new_text_4.txt', 'w', encoding='utf-8') as new_file:
    for el in new_content:
        print(el, file=new_file)
