import csv

f = open('daegu-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f, delimiter=',')
header = next(data)
print(header)

i = 1
for row in data:
    print(row)
    if i >= 5:
        break  # 5개의 데이터를 출력하면 break
    i += 1
f.close()