class Matrix:

    def __init__(self, list_object):
        self.list_object = list_object

    def __str__(self):
        for i in self.list_object:
            print(*i)
        return ''

    def __add__(self, other):
        sum_result = []
        for _ in range(len(self.list_object)):
            sum_result.append([])
        for i in range(len(self.list_object)):
            for j in range(len(self.list_object[0])):
                sum_result[i].append(0)

        for i in range(len(self.list_object)):
            for j in range(len(self.list_object[0])):
                sum_result[i][j] = self.list_object[i][j] + other.list_object[i][j]
        return Matrix(sum_result)


m1_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2_list = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
m1 = Matrix(m1_list)
m2 = Matrix(m2_list)
m3 = m1 + m2
print(m3)
m4 = m3 + m1
print(m4)
print(m4 + m1 + m3)
