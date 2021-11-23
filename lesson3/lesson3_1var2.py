number1 = input("Введите первое число: ")
number2 = input("Введите второе число: ")

try:
    number1 = int(number1)
    number2 = int(number2)
except (number1 == 0, number2 == 0) as err:
    print("err")
else:
        g = number1 / number2
        f = number2 / number1
        print(f"Деление первого на второе число = {round(g, 3)}")
        print(f"Деление второго на первое число = {round(f, 4)}")

