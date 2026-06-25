list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]

result = []

for a in list1:
    for b in list2:
        result.append(a * b)

print(result)
