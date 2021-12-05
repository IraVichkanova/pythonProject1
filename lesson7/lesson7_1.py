
class Matrix:
    def __init__(self, k):
        self.k = k
    def __str__(self):
        return '\n'.join('\t'.join([f"{item:3}" for item in line]) for line in self.k)

    def __add__(self, other):
      try:
          cente = [[int(self.k[line][item]) + int(other.k[line][item]) for item in range(len(self.k[line]))]
                   for line in range(len(self.k))]:
         return Matrix(cente)
      except IndexError:
          return f"Ошибка разности матриц"


first_matrix = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
second_matrix = [[3, 6, 22], [23, -10, 36], [0, 0, 8]]
matr1 = Matrix(first_matrix)
matr2 = Matrix(second_matrix)
print(f"Первая матрица\n{matr1}")
print(f"Вторая матрица\n{matr2}")
print(f"Итог\n{matr1+matr2}")


