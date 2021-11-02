# Сразу решил задание без создания списка
text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

index = 0

while True:
    if not text_list[index].isalpha():
        if text_list[index].isdigit():
            text_list[index] = text_list[index].zfill(2)
        else:
            text_list[index] = text_list[index][0] + '0' + text_list[index][1:]
        text_list.insert(index, '"')
        text_list.insert(index + 2, '"')
        index += 3
        continue
    index += 1

    if index == len(text_list):
        break
print(' '.join(text_list))
