from random import choice
class Car:
    direct = ["север", "юг", "запад", "восток",
              "северо-запад", "северо-восток", "юго-запад","юго-восток"]
    #атрибуты
    def __init__(self, sp, n, cl, isp=False):
        self.speed = sp
        self.name = n
        self.color = cl
        self.is_police = isp
    print(f"Выбранная машина: {n} окрашена в {cl} цвет.\n Явяляется ли машина полицейской? {isp}")
    #методы
    def go(self):
        print(f"Go {self.name}")
    def stop(self):
        print(f"Stop {self.name}")
    def turn(self, direction):
        print(f"{self.name}, please, turn to {choice(self.direct())}")
    def show_speed(self, speed):
        print(f"Текущая скорость автомобиля {self.name}: {speed}")
class TownCar(Car):
    #методы для подкласса класса
    def show_speed(self, speed):
        if speed >= 60:
            print(f"Превышение скорости! {self.name} Сбавьте обороты")
        else:
            print(f"Скорость TownCar {self.name} - {speed}")

class SportCar(Car):

class WorkCar(Car):
    def show_speed(self, speed):
        if speed >= 40:
            print("Превышение скорости! Сбавьте обороты")
        else:
            print(f"Скорость WorkCar {speed}")

class PoliceCar(Car):

    def __init__(self, sp, n, cl, isp=False):
        super().__init__(self, sp, n, cl, isp=False)

town_car = TownCar("Городская", "синий", 2020)
sport_car = SportCar("Спортивная", "желто-черный", 2021)
work_car = WorkCar("Рабочая", "синяя", 2016)
police_car = PoliceCar("Полицейская", "бела-синяя", 2017)

cataloge_cars = [town_car, sport_car, work_car, police_car]
for i in cataloge_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()