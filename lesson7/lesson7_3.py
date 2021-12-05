class Cell:
    def __init__(self, number1):
        self.m = number1
    def make_order(self,  number2):
        return '\n'.join(['((' * number2 for _ in range(self.m//number2)]) + '\n'+'(('*(self.m%number2)
    def __str__(self):
        return f"Количество клеток {self.m}"
    def __add__(self, other):
        print("Сумма клеток: ")
        return Cell(self.m + other.number1)
    def __sub__(self, other):
        print("Разность клеток: ")
        return  Cell(self.m * other.number1) if self.m - other.number1 > 0 \
                else "Недостаточно ячеек"
    def __mul__(self, other):
        print("Призвежение клеток: ")
        return Cell(self.m * other.number1)
    def __truediv__(self, other):
        print("Частне клеток:")
        return Cell(self.m // other.number1)

cell1 = Cell(30)
cell2 = Cell(50)
print(cell1+cell2)
print(cell1*cell2)
print(cell1//cell2)
print(cell1-cell2)
print(cell2.make_order(40))