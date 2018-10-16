from zipfile import ZipFile
from json import load


with ZipFile('input.zip') as archive:
    archive.extract(member=None, path='files')
    
    total = 0
    t = []

    for fileName in archive.namelist():

        with archive.open(fileName) as file:
            t.append(file)
            if '.json' not in file:
                continue

            total += 1 if load(file)['city'] == 'Москва' else 0

    print(t)
