vir = int(input("Введите значение выручки: "))
izd = int(input("Введите значение издержек: "))

if (vir-izd) > 0:
    print("Вы в прибыли")
elif (vir-izd) < 0:
    print("У вас убыток")
else:
    print("У вас стабильный 0")