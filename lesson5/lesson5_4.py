russian_interp= {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open('4task.txt', "r", encoding="utf-8") as new_file:
    with open('Урок5_задание4.txt', encoding="utf-8") as mother_file:
        new_file.writelines([line.replace(line.split()[0], russian_interp.get(line.split()[0])) for line in mother_file])
