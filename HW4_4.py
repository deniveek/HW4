import random


lst = [random.randint(1, 9) for _ in range(5)]
res = [i for i in lst if lst.count(i) == 1]
print(lst)
print(res)
