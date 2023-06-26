money = int(input("지폐로 교환할 돈은 얼마? "))


a = money // 50000
money %= 50000

b = money // 10000
money %= 10000

c = money // 5000
money %= 5000

d = money // 1000
money %= 1000

print("50000원 지폐: %d장" % a)
print("10000원 지폐: %d장" % b)
print("5000원 지폐: %d장" % c)
print("1000원 지폐: %d장" % d)
print("남은 지폐: %d원" % money)
