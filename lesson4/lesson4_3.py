from random import randint
first_list = [randint(20,240) for _ in range(1, randint(20,240))]
print(f"Исходный список чисел\n {first_list}")
itog = [el for el in range(20, 240) if el% 20 == 0 or el% 21 == 0]
print(f"Список чисел из генератора, которые кратны 20 или 21\n {itog}")
