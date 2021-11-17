src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [digit_2 for digit_1, digit_2 in zip(src, src[1:]) if digit_2 > digit_1]
print(result)
