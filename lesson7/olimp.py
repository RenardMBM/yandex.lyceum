import csv

with open('rez.csv', encoding='utf8') as res:
    reader = csv.reader(res, delimiter=',', quotechar='')
