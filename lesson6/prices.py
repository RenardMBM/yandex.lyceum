print(sum(
    [
        float(line.split('\t')[-1]) * int(line.split('\t')[1]) if line else 0
        for line in open('prices.txt', encoding='utf8').read().split('\n')
    ]
))
