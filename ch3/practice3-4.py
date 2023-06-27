i, sum, sum2 = 0, 0, 0

for i in range(0, 101, 1):
    if i % 7 == 0:
        sum = sum + i

print("0과 100 사이에 있는 7의 배수 함계 : %d" % sum)


for i in range(0, 101, 7):
    sum2 = sum2 + i

print("0과 100 사이에 있는 7의 배수 함계 : %d" % sum2)
