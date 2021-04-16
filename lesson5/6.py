result_dict = {}
raw_dict = {}
digit_list = []

with open('text_6.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()

for item in content:
    for idx, char in enumerate(item):
        if char == ':':
            raw_dict[item[:idx]] = item[idx + 1:]

for value in raw_dict.values():
    string = ''.join((char if char in '0123456789' else ' ') for char in value)
    digit_list.append(sum(map(int, string.split())))

for idx, key in enumerate(raw_dict.keys()):
    result_dict[key] = digit_list[idx]

print(result_dict)
