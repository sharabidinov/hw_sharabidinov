src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = set()
unique_num = set()
for el in src:
    if el not in tmp:
        unique_num.add(el)
    else:
        unique_num.discard(el)
    tmp.add(el)
sorted_unique_num =  [el for el in src if el in unique_num]
print(sorted_unique_num)
