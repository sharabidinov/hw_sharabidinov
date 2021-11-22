result = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for x in f:
        line = f.readline().split()
        data_tuple = (line[0], line[5][1:], line[6])
        result.append(data_tuple)
for data in result:
    print(data)
