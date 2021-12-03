class Road:
    #атрибуты
    def __init__(self, l, w):
        self._length = l
        self._width = w

    #метод расчета
    def count(self, m = 300, s = 20):
        self.mass = m
        self.sumthick = s
        return f"{self._length}м *{self._width}м *{m}кг *{s}см = "\
               f"{(self._length*self._width*m* s/1000)}"

road_1 = Road(3000,30)
print(road_1.count())
road_2 = Road(1000,150)
print(road_2.count())