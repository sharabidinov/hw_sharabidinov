class Matrix:

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return ' '.join(map(str, self.lst))

    def __add__(self, other):
        new_matrix = []
        for item in range(len(self.lst)):
            new_matrix.append([])
            for el in range(len(self.lst[0])):
                new_matrix[item].append(self.lst[item][el] + other.lst[item][el])
        return Matrix([new_matrix])


if __name__ == '__main__':
    a = [[5, 3, 1, 6], [4, 4, 4, 5], [9, 0, 5, 0]]
    b = [[1, 1, 1, 2], [2, 2, 2, 2], [3, 3, 3, 1]]
    matrx1 = Matrix(a)
    matrx2 = Matrix(b)
    result = matrx1 + matrx2
    print(result)
