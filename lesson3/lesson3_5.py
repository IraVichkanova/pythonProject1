itog = 0
while True:
    z = input("Введите строку чисел или спецпиальный прерывающий знак R для выхода")
    tokens = z.split(" ")
    for token in tokens:
        try:
            numbers = float(token)
            itog += numbers
        except:
            if token == 'R':
                print(f"Сумма до ошибки =  {itog}. Программа окончена. Спасибо")
                exit(0)
            else:
                print(f"Итоговая сумма после ошибки {itog}")
                exit(1)