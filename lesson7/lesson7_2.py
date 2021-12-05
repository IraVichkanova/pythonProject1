class VarClothes:
    r = 0
    def __init__(self, v, h):
        self.size = v
        self.heigth = h

    @property
    def result(self):
        pass

    def __add__(self, other):
        VarClothes.r += self.result + other.result
        return Suit(0)

    def __srt__(self):
        d = VarClothes.result
        VarClothes.result = 0
        return f"{d}"


class Coat(VarClothes):
    @property
    def result(self):
        return round(self.size/6.5 + 0.5)

class Suit(VarClothes):
    @property
    def result(self):
        return round((2*self.heigth + 0.3)/100)

coat_1 = Coat(30, 170)
suit_1 = Suit(10, 180)
suit_2 = Suit(40, 150)
print(coat_1 + suit_1 + suit_2)