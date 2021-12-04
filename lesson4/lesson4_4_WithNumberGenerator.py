from random import randint
first_list = [randint(-15, 15) for _ in range(17)]
print(f"Исходная последовательность цифр\n{first_list}")
res = [el for el in first_list if first_list.count(el) == 1]
print(f"Результат отбора\n{res}")