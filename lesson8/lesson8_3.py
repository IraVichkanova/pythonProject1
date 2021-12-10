class Wrong_number:
    def __init__(self, *args):
        self.number_1 = []

    def sost_check(gh):
        while True:
            try:
                symb = int(input("Введите значени и нажмите Enter для продолжения работы"))
                self.number_1.append(symb)
                print(f"Список на данный момент {self.number_1}\n")
            except:
                print("Введеная информация строка")
                ag = input("Продолжаем? Если нет, введите stop, если да cont")

            if ag == "stop" or ag == "STOP" or ag == "Stop":
                print(first.sost_check())
            elif ag == "cont" or ag == "CONT":
                return "Все закончилось"
            else:
                return "Все закончилось"

first = Wrong_number(3)
print(first.sost_check())
