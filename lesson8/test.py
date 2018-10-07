from zipfile import ZipFile
with ZipFile('archive.zip', 'w') as myzip:
    myzip.write('test.txt')
