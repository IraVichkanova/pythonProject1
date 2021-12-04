first_sl = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"Исходная последовательность чисел\n{first_sl}")

dictionary = {i: 0 for i in first_sl}
for i in first_sl:
    dictionary[i] +=1

print([i for i in dictionary if dictionary[i] == 1])