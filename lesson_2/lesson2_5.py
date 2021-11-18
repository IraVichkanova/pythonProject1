my_list = [1, 5, 8, 2, 4]
print(my_list)
number = int(input("Введите любую цифру (выход из всего 121): "))
print(number)
n = 0
for el in range(len(my_list)):
        if number == my_list[el]:
            my_list.insert(el+1, number)
            print(f"Новая последовательность: ", my_list)
        elif number > my_list[0]:
            my_list.insert(0, number)
        #elif number < (my_list[-1]):
            #my_list.append(number)
        elif number < my_list[el] and number > my_list[el+1]:
            my_list.isert(el+1, number)
            print(f"Последовательность после изменения: ", my_list)

             #my_list.count(number)
             #c = my_list.count(number)
             #print(f"Первое место заданного числа - ", c)
             #my_list.insert(c, number)
             #my_list.index(number)
             #my_list[-1]


