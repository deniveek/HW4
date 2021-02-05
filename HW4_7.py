def fact(number):
    res = 1
    for i in range(1, number+1):
        res = res * i
        yield res


for n in fact(10000):
    print(n)
