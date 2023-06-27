i, j = 0, 0


for i in range(1, 10, 1):
    print("##  %d단 ##" % i)
    for j in range(1, 10, 1):
        print("%d X %d = %d" % (i, j, i * j))
