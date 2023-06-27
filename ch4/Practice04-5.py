A = input("문자열 입력: ")

if A.isdigit():
    print("숫자입니다.")
elif A.isalpha():
    print("글자입니다.")
elif A.isalnum():
    print("글자+숫자입니다.")
else:
    print("모르겠습니다.")
