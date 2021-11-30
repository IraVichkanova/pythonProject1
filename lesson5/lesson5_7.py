import json

with open('task7.json', 'w', encoding='utf-8') as json_file:
    with open("Урок5_задание7_фирмы.txt", encoding="utf-8") as f_file:
       profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_file}
       result = [profit, {"Средняя выручка": round(sum([int(i) for i in profit.values() if int(i)>0]) /
                                                   len([int(i) for i in profit.values() if int(i) >0]))}]
    json.dump(result, json_file, ensure_ascii=False, indent=4)

