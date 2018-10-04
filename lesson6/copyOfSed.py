text = open(input(), encoding='utf8').read().split('\n')
newFile = open('output.txt', 'w')
command = input().split()
a, b = command[-2], command[-1]

