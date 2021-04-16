with open('text_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(f'Строк содержится в файле: {len(lines)}')
for ind, line in enumerate(lines, 1):
    print(f'{ind} строка - {len(line.split())} слов.')
