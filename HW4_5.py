from functools import reduce

ls = [i for i in range(100, 1001, 2)]
print(reduce(lambda a, b: a * b, ls))
