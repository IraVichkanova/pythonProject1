class Stationery:
    def __init__(self, title = "Сегодня мы что-то создадим"):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки! {self.title}")

class Pen(Stationery):
      def draw(self):
        print(f"Сегодня выполняем варианты принта {self.title}")
class Pencil(Stationery):
      def draw(self):
        print(f"Сегодня работаем с гафикой {self.title}")
class Handle(Stationery):
      def draw(self):
        print(f"Сегодня день мастерства {self.title}! Удачи!")

status = Stationery()
pen = Pen("JBF")
pencil = Pencil("PLJH")
handle = Handle("BHBY")

itog_in_office = [status, pen, pencil, handle]
for i in itog_in_office:
    i.draw()