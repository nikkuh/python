from functools import reduce


def multi(j, k):
    return j * k


print(reduce(multi, (n for n in range(100, 1001) if not n % 2)))
