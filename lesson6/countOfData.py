from collections import Counter

count = [1 if float(number) > 0 else -1 if float(number) < 0 else 0
         for line in open('input.txt', encoding='utf8').read().split('\n')
         for number in line.split()]

count = Counter(count)
newFile = open('output.txt', 'w')
print(len(count), file=newFile)
print(*[str(_) + ' ' + str(count[_]) for _ in [1, -1, 0] if count[_]], file=newFile)
newFile.close()
