lst = []
for item in range(1, 1001, 2):
    lst.append(item ** 3)

total_sum = 0
for element in lst:
    sum_1 = 0
    total = element
    while element != 0:
        sum_1 += element % 10
        element //= 10
    if sum_1 % 7 == 0:
        total_sum += total
print(total_sum)

total_sum = 0
for element in lst:
    sum_1 = 0
    element += 17
    total = element
    while element != 0:
        sum_1 += element % 10
        element //= 10
    if sum_1 % 7 == 0:
        total_sum += total
print(total_sum)
