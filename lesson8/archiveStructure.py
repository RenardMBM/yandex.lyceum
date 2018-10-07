from zipfile import ZipFile


def human_read_format(fileSize):
    return str(fileSize) + 'Б' if fileSize < 1024 else \
        str(round(fileSize / 1024)) + 'КБ' if fileSize < 1024 ** 2 else \
        str(round(fileSize / 1024 ** 2)) + 'МБ' if fileSize < 1024 ** 3 else \
        str(round(fileSize / 1024 ** 3)) + 'ГБ'


with ZipFile('input.zip') as archive:
    info = archive.infolist()
    fileNumber = 0

    for file in archive.namelist():
        way = file.split('/')
        name = way[-1] if way[-1] else way[-2]
        size = ' ' + human_read_format(info[fileNumber].file_size) if '.' in name else ''
        print(('  ' * (file.count('/') - 1 if file[-1] == '/' else file.count('/'))) + name + size)
        fileNumber += 1
