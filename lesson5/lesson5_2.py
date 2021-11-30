with open("Урок5_задание2.txt", encoding="utf-8") as txt:
    line = txt.readlines()
    for index, value in enumerate(line, 1):
        num_of_words = len(value.split())
        print(f'Строка {index} сожержит {num_of_words} слов')