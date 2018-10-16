import os
import shutil
from datetime import datetime
from shutil import move


def make_reserve_arc(source, destination):
    if source == '.' or not source:
        directoryWithSource = os.getcwd()

    else:
        directoryWithSource = source.replace('\\', '/') if '\\' in source else source

    directoryWithResult = destination.replace('\\', '/') if '\\' in destination else destination

    fileName = 'a copy of ' +\
               directoryWithSource.split('/')[-1] +\
               ' made in ' +\
               '-'.join(str(datetime.now()).split('.')[0].split(':'))

    shutil.make_archive(fileName, 'zip', root_dir=directoryWithSource)
    if destination != '.' and destination:
        move(fileName + '.zip', directoryWithResult)


make_reserve_arc(input('Введите путь к каталогу, который надо архивировать:\n'),
                 input('Введите путь к существующему каталогу,'
                       ' в который необходимо поместить результат:\n'))
