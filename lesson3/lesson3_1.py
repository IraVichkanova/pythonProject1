def m_substraction(s_1, s_2):
    if (s_1 != 0) and (s_2 != 0):
        g = s_1 / s_2
        f = s_2 / s_1
        print(f"Деление первого на второе число = {round(g, 3)}")
        print(f"Деление второго на первое число = {round(f, 4)}")

m_substraction(float(input("Введите первое число s_1: ")), float(input("Введите второе число s_2: ")))