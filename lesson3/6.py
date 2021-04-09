def int_func(word):
    for lit in word:
        if ord(lit) not in range(97, 123):
            return None
    return word.title()


in_sentence = input('Введите разделённые пробелами слова из латинских букв нижнего регистра.').split()
out_sentence = []
for word in in_sentence:
    if int_func(word):
        out_sentence.append(int_func(word))

print(*out_sentence)
