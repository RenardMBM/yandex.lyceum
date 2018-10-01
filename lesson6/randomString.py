import random

length = len(open('lines.txt', encoding='utf8').read().split('\n'))

if length:
    print(open('lines.txt', encoding='utf8').read().split('\n')[random.randint(0, length - 1)])
