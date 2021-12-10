class DivByNull:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    @staticmethod
    def div_by_null(number_1, number_2):
        if number_2 != 0:
            return number_1/number_2
        else:
            return "Деление на ноль невозможно"

first_tr = DivByNull(13, 38)
print(DivByNull.div_by_null(10, 0))
print(DivByNull.div_by_null(13, 168))
print(first_tr.div_by_null(100, 8))