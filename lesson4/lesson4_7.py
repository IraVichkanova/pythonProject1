def general_number(num):
    t_num = 1
    for i in range(num + 1):
        yield f'{i}! = {t_num}'
        t_num *= i + 1


for el in general_number(int(input('Значение факториала: '))):
    print(el)