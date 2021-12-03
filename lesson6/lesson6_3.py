class Worker:
    #атрибуты
    def __init__(self, n, sur, pos, wage, bonus):
        self.name = n
        self.surname = sur
        self.position = pos
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    #методы для подкласса класса
    def get_full_name(self):
        return f"Полное имя сотрудника: {self.name} {self.surname}"
    def get_total_income(self):
        return f"{sum(self._income.values())}"

secretarian = Position("Anna", "Black", "helper", 2000, 4500)
print(secretarian.get_full_name())
print(secretarian.position)
print(secretarian.get_total_income())

