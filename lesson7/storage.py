import csv

with open('wares.csv', encoding='utf8') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')
    goods = {}

    for i, row in enumerate(reader):
        if not row:
            break

        goods[row[0]] = int(row[1])

    correctsGoods = sorted([_[0] for _ in goods.items() if _[1] <= 1000], key=lambda x: goods[x])
    outGoods = []

    if correctsGoods:

        for item in correctsGoods:
            n = 1000 // goods[item] if 1000 // goods[item] < 11 else 10
            outGoods += [item] * n

        print(*outGoods, sep=', ')

    else:
        print('error')
