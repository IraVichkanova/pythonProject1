time = int(input("Введите время в секундах: "))
num_sec = time % 60
num_hour = time // 3600
num_min = time // 60 - num_hour * 60
print(f"Время, которое ввели {num_hour:02}:{num_min:02}:{num_sec:02}")