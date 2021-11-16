src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

'''Я реализовал два способа реализации, первая с помощью set, вторая с помощью лист. Разница в том что при реализации 
через set мы не сможем сохранить последовательность как в списке, но она работает намного быстрее списка. '''
tmp = set()
unique_num = set()
for el in src:
    if el not in tmp:
        unique_num.add(el)
    else:
        unique_num.discard(el)
    tmp.add(el)
print(unique_num)

unique_num_lst = [num for num in src if src.count(num) == 1]
print(unique_num_lst)
