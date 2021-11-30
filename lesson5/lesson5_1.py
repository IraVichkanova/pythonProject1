
with open("my_first_file.txt", "w", encoding="utf-8") as first_file:
    while True:
        l = input('Введите строку или пустую строку: ')
        if not l:
            break
        print(l, file=first_file)
