class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        itog_MyDate = day_month_year
        #for i in day_month_year.split('-'):
            #if i != '-':
                #itog_MyDate.append()
                #return int(itog_MyDate[0]), int(itog_MyDate[1]), int(itog_MyDate[2])
        result_list = day_month_year.split('-')
        if itog_MyDate[0] >=1 and itog_MyDate[0] <=31:
            if itog_MyDate[1] <= 12 and itog_MyDate[1] >= 1:
                if itog_MyDate[0] >29 and itog_MyDate[1] == 2:
                    return result_list
                else:
                    return "Такая дата в феврале несуществет"
            else:
                return "Вы ввели неправильный месяц"
        else:
            return "Такого дня не существует"



    @staticmethod
    def valid(day, month, year):
        if day >=1 and day<= 31:
            if month >=1 and month<=12:
                if year>=0 and year<=2021:
                    return "Введеная дата существует"
                else:
                    return "Такой год еще не наступил"
            else:
                return "Такого меясца не существует"
        else:
            return "Такого дня не существует"
    def __str__(self):
        return f"Дата на данный момент {Data.extract(self.day_month_year)}"

Data_for_today = Data('05-1-2021')
print(Data_for_today)
