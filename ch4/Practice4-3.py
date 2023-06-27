i, j, value, list1, list2 = 0, 0, 0, [], []


for i in range(0, 5):
    for j in range(0, 5):
        list1.append(value)
        value += 3
    list2.append(list1)
    list1 = []

print(list2)

for i in list2:
    print(i, end=" ")
    print("")

for i in range(0, 4):
    for j in range(0, 5):
        print("%2d" % list2[i][j], end=" ")
    print("")
