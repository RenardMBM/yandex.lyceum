import csv

with open('rez.csv', encoding='utf8') as res:
    a = []
    schools = {}
    reader = csv.reader(res, delimiter=',', quotechar='"')

    for index, row in enumerate(reader):
        if not row:
            continue

        r = row[2].split('-')

        if r[2] in schools:

            if r[3] in schools[r[2]]:
                schools[r[2]][r[3]].append((row[1], row[-1]))

            else:
                schools[r[2]][r[3]] = [(row[1], row[-1])]

        else:
            schools[r[2]] = {r[3]: [(row[1], row[-1])]}

    nSchool, nRoom = input().split()

    if nSchool in schools:

        if nRoom in schools[nSchool]:
            correctP = sorted(schools[nSchool][nRoom], key=lambda x: (
                x[1], -int(''.join([
                    str(ord(_)) for _ in x[0]
                ]))
            ))

            for p in correctP:
                print(*p)

        else:
            print('error incorrect number of room')

    else:
        print('error incorrect number of school')
