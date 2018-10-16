import csv

with open('input.csv') as file:
    correctWays = []
    ways = {}
    reader = csv.reader(file, delimiter=';', quotechar='"')

    for index, string in enumerate(reader):
        startPoint, endPoint, cost = string

        if not cost:
            startPosition, endPosition = startPoint, endPoint
            break

        ways.setdefault(startPoint, []).append((endPoint, int(cost)))

    for firstPoint, firstCost in ways[startPosition]:

        if firstPoint == endPosition:
            correctWays.append((
                startPosition,
                firstPoint,
                int(firstCost)
            ))
            continue

        for secondPoint, secondCost in ways[firstPoint]:

            if secondPoint == endPosition:
                correctWays.append((
                    startPosition,
                    firstPoint,
                    secondPoint,
                    int(firstCost) + int(secondCost)
                ))

    print(*min(*correctWays, key=lambda x: x[-1])[:-1])
