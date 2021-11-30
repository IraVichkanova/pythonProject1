my_dictionary = {}
with open("Урок5_ задание6_словарь.txt", encoding="utf-8") as txtx:
    for line in txtx:
        name, status = line.split(':')
        sum = sum(map(int, "".joint([i for i in status if i == ' ' or '9' >= i >= '0']).split()))
        my_dictionary[name] = sum
print(f"{my_dictionary}")