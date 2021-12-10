class Sklad:
    def __init__(self, h, w, s):
        self.hight = h
        self.width = w
        self.long = s

    def __str__(self):
        res = self.long*self.width*self.hight
        return f"Размеры склада {self.long} * {self.width} * {self.hight} = {res}"

class Orgtechnic:
    def __init__(self, wow):
        self.amountOfTech = wow
        print(f"Общее кол-во единиц техники {self.amountOfTech}")
    #def scan_to(self):
        #print(f"Сканировать {self.amountOfTech}\15 страниц!")

    #def print_to(self):
        #print(f"Печатать {self.amountOfTech}\17 страниц!")

    #def xser_to(self):
       # print(f"Отправлять {self.amountOfTech}\10 страниц!")

class Scaner(Orgtechnic):
    def scan_to(self):
        print(f"Сканировать {self.amountOfTech}\15 страниц!")

class Printer(Orgtechnic):
    def print_to(self):
        print(f"Печатаь 1  {self.amountOfTech}\17 страниц!")

class Xserox(Orgtechnic):
    def xser_to(self):
        print(f"Отправлять 3  {self.amountOfTech}\10 страниц!")

first = Sklad(10, 89, 120)
print(first)
number_of_t = Orgtechnic(500)
print(Scaner.scan_to(number_of_t))
print(Printer.print_to(number_of_t))
print(Xserox.xser_to(number_of_t))