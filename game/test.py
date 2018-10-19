# from sapper import generateBomb, findLocationOfObject
from settings import *
from cell import Cell
from random import randint

field = []

for r in range(1, ROW + 1):
    row = []

    for c in range(1, COLUMN + 1):
        row.append(Cell(c * CELL_SIZE_X + OFFSET_FROM_EDGE,
                        r * CELL_SIZE_Y + OFFSET_FROM_EDGE))
        # print(row)
    field.append(row)


def generateBomb(x, y):
    field[y][x].isBomb = True

    for y1 in [y - 1, y, y + 1]:

        if y1 < 0 or y1 == ROW:
            continue

        for x1 in [x - 1, x, x + 1]:

            if x1 < 0 or x1 == COLUMN:
                continue

            alveolus = field[y1][x1]
            alveolus.numberOfBombNear += 1


isFirstPress = True
if isFirstPress:
    isFirstPress = False
    xCell, yCell = 5, 7

    for nBomb in range(NUMBER_OF_BOMB):
        randomY, randomX = randint(0, ROW - 1), randint(0, COLUMN - 1)

        while randomX == xCell:
            randomX = randint(0, COLUMN - 1)

        while randomY == yCell:
            randomY = randint(0, ROW - 1)

        generateBomb(randomX, randomY)
