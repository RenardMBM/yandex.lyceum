import os


def human_read_format(size):
    return str(size) + 'Б' if size < 1024 else \
        str(round(size / 1024)) + 'КБ' if size < 1024 ** 2 else \
        str(round(size / 1024 ** 2)) + 'МБ' if size < 1024 ** 3 else \
        str(round(size / 1024 ** 3)) + 'ГБ'


def get_files_sizes():
    return '\n'.join([file + ' ' + human_read_format(os.stat(file).st_size)
                      for file in os.listdir(path='.') if file != '__pycache__'])
