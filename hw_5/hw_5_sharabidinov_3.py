from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(tutors) > len(klasses):
    tuple_gen = (items for items in zip_longest(tutors, klasses, fillvalue=None))
else:
    tuple_gen = (items for items in zip(tutors, klasses))

print(type(tuple_gen))
print(type(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
print(next(tuple_gen))
