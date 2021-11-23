
def catalog():
    name = str(input("Введите имя: "))
    sname = str(input("Введите фамилию: "))
    birthyear = str(input("Введите год рождения: "))
    mcity = str(input("Введите город проживания: "))
    email = input("Введите email: ")
    phonenumber = int (input("Введите свой телефон: "))
    result = (name, sname, birthyear, mcity, email, phonenumber)
    return result
v = catalog()
print(v)


