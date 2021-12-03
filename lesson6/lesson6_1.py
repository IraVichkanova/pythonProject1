from time import sleep

class TrafficLight:
    #атрибут color
    def __init__(self, color):
        __color = color

    #методы running
    def running(self):
            print("Включен красный сигнал светофора")
            sleep(7)
            print("Включен желтый сигнал светофора")
            sleep(2)
            print("Включен зеленый сигнал светофора")
            sleep(10)
            print("Включен желтый сигнал светофора")
            sleep(2)

