from itertools import count, cycle
"""Variant a"""
f = int(input("Введите стартовое число "))
for el in count(f):
    if el >= 20:
        break
    else:
        print(el)

"""Variant b"""
for el in cycle(f):
    if f >=10:
        break
    print(el)
    f +=1.5