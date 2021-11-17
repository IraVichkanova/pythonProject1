numer_init = int(input("Введите положительное число "))
max = 0
num = numer_init

while num > 0:
    last = num % 10
    if last > max:
        max = last
        if max == 9:
            break
        num = num // 10

print(f"Максимальная цифра в числе {numer_init} = {max}")