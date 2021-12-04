starter = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [starter[num] for num in range(1, len(starter)) if starter[num] > starter[num-1]]
print(new_list)