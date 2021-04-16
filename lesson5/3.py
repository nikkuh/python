with open('text_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

for line in lines:
    line = line.split()
    if float(line[1]) < 20000:
        print(f'Сотрудник {line[0]} имеет зарплату {line[1]}.')
