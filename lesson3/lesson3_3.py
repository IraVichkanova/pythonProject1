def m_func(s_1, s_2, s_3):
    pac = [s_1, s_2, s_3]
    bet = []
    max1 = max(pac)
    bet.append(max1)
    pac.remove(max1)
    max2 = max(pac)
    bet.append(max2)
    pac.remove(max2)
    print(f"Сумма двух наибольших числе= {sum(bet)}")
m_func(int(input("Введите первое число s_1: ")), int(input("Введите второе число s_2: ")), int(input("Введите второе число s_3: ")))