import random


random_list = [random.randint(0, 999) for i in range(30)]   #список из 30 случайных чисел
reduced = [random_list[i] for i in range(1, len(random_list)) if random_list[i] > random_list[i-1]]

print(random_list)
print(reduced)
