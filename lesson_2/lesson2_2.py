my_listnumber = input("Введите любую последовательность цифр: ").split()
print(my_listnumber)
print(len(my_listnumber))
for b in range(0, len(my_listnumber)-1, 2):
    my_listnumber[b], my_listnumber[b+1]= my_listnumber[b+1], my_listnumber[b]
print(my_listnumber)

