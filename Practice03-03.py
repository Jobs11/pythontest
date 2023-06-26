a = int(input("첫 번째 숫자를 입력하세요: "))
b = int(input("두 번째 숫자를 입력하세요: "))
c = int(input("더할 숫자를 입력하세요: "))

sum = 0
for i in range(a, b + 1, c):
    sum = sum + i

print("%d + %d + .... + %d는 %d입니다." % (a, a + c, i, sum))
