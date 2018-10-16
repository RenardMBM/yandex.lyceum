import os


def getWeightOfFolder(way):
    return sum([os.stat(way + '/' + file).st_size if '.' in file
                else getWeightOfFolder(way + '/' + file)
                for file in os.listdir(path=way)])


def human_read_format(size):
    return str(size) + 'Б' if size < 1024 else \
        str(round(size / 1024)) + 'КБ' if size < 1024 ** 2 else \
        str(round(size / 1024 ** 2)) + 'МБ' if size < 1024 ** 3 else \
        str(round(size / 1024 ** 3)) + 'ГБ'


fileSizes = dict()

for fileName in os.listdir('.'):
    fileSizes[str(fileName)] = os.stat(fileName).st_size\
        if '.' in fileName else getWeightOfFolder(os.getcwd())

top = sorted([file for file in fileSizes.items()], key=lambda x: (-x[-1], x[0]))[:10]
maxLen = len(max(*top, key=lambda x: len(x[0]))[0])

print('\n'.join([
    name + (maxLen - len(name) + 7) * ' ' + '-' + human_read_format(size)
    for name, size in top
]))
