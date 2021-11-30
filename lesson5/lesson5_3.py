with open("Урок5_задание3_сотрудники.txt", "w", encoding="utf-8") as txtx:
    txtx.writelines(f"Самсонов {2903}\nЯхтр {200}\nШепелев {10}\nБаурн {2}\n")
    workers = {}
    for line in txtx:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}:Зарплата меньше 20000')


