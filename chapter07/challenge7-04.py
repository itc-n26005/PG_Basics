answers = [3, 7, 15, 20]

while True:
    s = input("数字を入力（終了は q）: ")

    if s == "q":
        print("終了します")
        break

    elif s.isdigit():
        n = int(s)

        if n in answers:
            print("正解")
        else:
            print("不正解")

    else:
        print("数字を入力するか、qで終了します")
