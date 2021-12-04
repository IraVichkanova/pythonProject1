def start_of_operation():
    print("Ниже будет заработная плата сотрудника")

def result():
   salinhour = int(input("Ввелите цену выработки в часах: "))
   payforhour = int(input("Введите значение ставки в час: "))
   extra = int(input("Введите значение премии: "))
   return salinhour*payforhour + extra
