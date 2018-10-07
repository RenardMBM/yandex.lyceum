from zipfile import ZipFile
from json import load

with ZipFile('input.zip') as archive:
    total = 0

    for fileName in archive.namelist():

        with open(fileName) as file:
            total += 1 if load(file)['city'] == 'Москва' else 0

    print(total)
