from random import randint
with open('task5.txt',  mode='w+', encoding='uft-8') as tsk5:
    tsk5 = [randint(1, 1000) for _ in range(1000)]
    tsk5.write(" ".joint(map(str, tsk5)))
print(f"Сумма элементов - {sum(tsk5)}")
