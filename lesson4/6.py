from itertools import count, cycle

c = 1
for n in count(5, 1.5):
    print(n)
    c += 1
    if n > 25:
        break

b = 1
for lit in cycle('qu'):
    print(lit)
    b += 1
    if b == 15:
        break
