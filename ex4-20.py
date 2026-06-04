a = input("数字を入力してください")
b = input("別の数字を入力してください")
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print("b cannot be zero.")

