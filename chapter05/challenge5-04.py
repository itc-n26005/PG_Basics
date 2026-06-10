anything = {
   "height" : "172cm",
   "color"  : "white",
   "singer" : "SUPER BEAVER",
}

key = input("キーを入力してください:")
if key in anything:
    anything = anything[key]
    print(anything)
else:
    print("見つかりません。")


