from sys import argv

def Result():
    try:
        hour, pay, bonus = map(float, argv[1:])
        print(f"Итоговая зарплата сотрудника - {hour*pay+bonus}")
    except ValueError:
        print("Введите три числа для расчета зарплаты сотрудника через пробел")