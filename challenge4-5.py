def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None

print(to_float("3.14"))
print(to_float("abc"))

"""
float型に変換して返す
 変換できなかったらNoneを返す
 s : 変換の文字列
  変換できたらfloat、できなかったらNone
  """
