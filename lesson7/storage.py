import csv

with open('wares.csv', encoding='utf8') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')
    goods = {}

    for i, row in enumerate(reader):
        if not row:
            break

        goods[row[0]] = int(row[1])

    correctsGoods = [_[0] for _ in goods.items() if _[1] <= 1000]

    if correctsGoods:
        print(*[item for item in sorted(goods, key=lambda x: (goods[x], x)) if item in correctsGoods])
    else:
        print('error')
