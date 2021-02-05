from itertools import cycle

ctr = 0
ls = ["1", "2", "3"]
for i in cycle(ls):
    if ctr > 15:
        break
    print(i)
    ctr += 1
