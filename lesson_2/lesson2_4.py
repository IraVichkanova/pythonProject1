my_list = input("Введите несколько слов через пробел: ")
print(my_list)
my_list.split(" ")
print(my_list)
for i, v in enumerate(my_list, 1):

    if len(str(my_list)) <=10:
       print(f"{i}) {v}")
else:
    print(f"{i}) {v} [0:10]")

