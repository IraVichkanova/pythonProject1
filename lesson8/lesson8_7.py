class Complex_Number:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.res = 'a + b*i'

    def __add__(self, other):
        print(f"Summary {self.a} and {self.b} equal = {self.a + other.a}+ {self.b + other.b}*i")
    def __mul__(self, other):
        print(f"Умножение чисел {self.a} и {self.b} = {self.a*other.b - (self.a*other.b)} + {self.b * other.a}*i")
    def __str__(self):
        return f" res322 = {self.a}+{self.b}*i"


p1 = Complex_Number(2, -4)
p2 = Complex_Number(10, 15)
print(p1 + p2)
print(p1*p2)
print(p1, p2)
