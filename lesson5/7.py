import json

result_list = []
inner_dict = {}
average_dict = {}
profit_list = []
profit_quantity = 0

with open('text_7.txt', 'r', encoding='utf-8') as file:
    content = file.read().split('\n')

for line in content:
    profit_list.append(int(line.split()[-2]) - int(line.split()[-1]))

for idx, text in enumerate(content):
    inner_dict[text.split()[0]] = profit_list[idx]

for key in inner_dict.values():
    if key > 0:
        profit_quantity += 1

average_dict['average_profit'] = (sum(d for d in profit_list if d > 0)) / profit_quantity
result_list.append(inner_dict)
result_list.append(average_dict)
with open('text_777.json', 'w', encoding='utf-8') as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)
