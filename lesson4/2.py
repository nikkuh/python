src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [x2 for x1, x2 in zip(src, src[1:]) if x2 > x1]
print(result)
