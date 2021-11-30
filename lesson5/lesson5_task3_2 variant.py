with open("Урок5_задание3_сотрудники.txt", "r", encoding="utf-8") as txtx:
    workers_dic={line.split()[0]: float(line.split()[1]) for line in txtx}
    print(f'Средняя зарплата = {round(sum(workers_dic.values())/ len(workers_dic), 3)}\n'
          f'Работники с зарплатой меньше 20000 {[i[0] for i in workers_dic.items() if i[1] < 20000]}')
