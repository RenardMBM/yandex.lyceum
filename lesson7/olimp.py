import csv

with open('rez.csv', encoding='utf8') as res:
    students = {}
    reader = csv.reader(res, delimiter=',', quotechar='"')
    numberOfSchool, numberOfClass = input().split()

    for index, row in enumerate(reader):

        if not row or '-' not in row[2]:
            continue

        login = row[2].split('-')

        if int(login[2]) == int(numberOfSchool) and int(login[3]) == int(numberOfClass):
            students.setdefault(row[-1], []).append(row[1].split()[3])

    for score in sorted(students.keys())[::-1]:

        for surname in sorted(students[score])[::-1]:
            print(surname, score)
