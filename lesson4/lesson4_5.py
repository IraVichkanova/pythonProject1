from functools import reduce

def itog_vsego(num_1, num_2):
    return num_1*num_2

result = [el for el in range(100, 1001, 2)]
print(f"Список чисел, с которыми мы работаем\n{result}")
print(f"После всех преобразований вот результат\n{reduce(itog_vsego, result)}")