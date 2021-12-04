from itertools import count
from math import factorial

def generator(number):
    num = 1
    for el in range(number+1):
        yield f'{el}! = {num}'
        num *= el+1

for i in generator(int(input("Введите число, до которого хотите найти факториал: "))):
    print(i)



