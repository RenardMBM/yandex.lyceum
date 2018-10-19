import pygame
from random import randint
from settings import *
from cell import Cell
from PIL import Image


def cellSearchByCoordinate(x, y):
    for line in field:

        for alveolus in line:

            if alveolus.x - CELL_SIZE_X <= x <= alveolus.x and alveolus.y - CELL_SIZE_Y <= y <= alveolus.y:
                return alveolus


def restartGame():
    global isGameOver, isFirstPress, isWin, coordinateOfFlags, coordinateOfBombs

    isFirstPress = True
    isGameOver = False
    isWin = False
    coordinateOfFlags = []
    coordinateOfBombs = []

    for line in field:

        for alveolus in line:
            alveolus.isBomb = False
            alveolus.mode = 0
            alveolus.numberOfBombNear = 0
            alveolus.nameImage = 'closed_cell.png'
            alveolus.isCheck = False


def findLocationOfObject(obj):
    for _ in range(len(field)):
        try:
            return field[_].index(obj), _

        except ValueError:
            continue


# def discoveryCellWithNumberOfBomb(indexOfList, indexOfCell):
#     total = 0
#     field[indexOfList][indexOfCell].isCheck = True
#
#     for iList in (indexOfList - 1, indexOfList, indexOfList + 1):
#
#         if iList == -1 or iList == ROW:
#             continue
#
#         for iCell in (indexOfCell - 1, indexOfCell, indexOfCell):
#
#             if (iList == indexOfList and iCell == indexOfCell) or iCell == -1 or iCell == COLUMN:
#                 print(indexOfList, indexOfCell)
#                 print(iList == indexOfList, iCell == indexOfCell, Cell == -1, iCell == COLUMN)
#                 continue
#
#             alveolus = field[iList][iCell]
#
#             if alveolus.isBomb:
#                 total += 1
#                 continue
#
#             if not alveolus.isCheck:
#                 discoveryCellWithNumberOfBomb(iList, iCell)
#
#     alveolus = field[indexOfList][indexOfCell]
#     alveolus.numberOfBombNear += total
#     alveolus.mode = 1

def generateBombs():
    global coordinateOfBombs

    for nBomb in range(NUMBER_OF_BOMB):
        y, x = randint(0, ROW - 1), randint(0, COLUMN - 1)

        while (x, y) in coordinateOfBombs or y == yCell or x == xCell:
            x, y = randint(0, COLUMN - 1), randint(0, ROW - 1)

        coordinateOfBombs.append((x, y))

        field[y][x].isBomb = True

        for y1 in [y - 1, y, y + 1]:

            if y1 < 0 or y1 == ROW:
                continue

            for x1 in [x - 1, x, x + 1]:

                if x1 < 0 or x1 == COLUMN:
                    continue

                alveolus = field[y1][x1]
                alveolus.numberOfBombNear += 1


def openCell(x, y):
    alveolus = field[y][x]
    alveolus.mode = 1
    alveolus.isCheck = True
    alveolus.drawCell()

    if not alveolus.numberOfBombNear:
        for y1 in (y - 1, y, y + 1):

            if y1 < 0 or y1 == ROW:
                continue

            for x1 in (x - 1, x, x + 1):

                if (y1 == y and x1 == x) or x1 < 0 or x1 == COLUMN:
                    continue

                alveolus = field[y1][x1]

                if alveolus.isCheck or alveolus.isBomb:
                    continue

                if alveolus.numberOfBombNear:
                    alveolus.mode = 1
                    alveolus.drawCell()

                else:
                    openCell(x1, y1)


def drawGameOverBackgroundAndGameOver():
    sc.blit(backgroundGameOver_surf, backgroundGameOver_rect)

    if isWin:
        sc.blit(win_surf, win_rect)

    else:
        sc.blit(gameOver_surf, gameOver_rect)


isOn = True
isMenuOn = True
isFirstPress = True
isGameOver = False
isWin = False

clock = pygame.time.Clock()
sc = pygame.display.set_mode((BACKGROUND_SIZE_X, BACKGROUND_SIZE_Y))

pygame.display.set_caption('Сапер')
img = Image.open('images/backgroundGameOver.png')
resized_img = img.resize((BACKGROUND_SIZE_X, BACKGROUND_SIZE_Y), Image.ANTIALIAS)
resized_img.save('images/resizeBackgroundGameOver.png')

background_surf = pygame.image.load('images/background.jpg')
background_rect = background_surf.get_rect(bottomright=(BACKGROUND_SIZE_X, BACKGROUND_SIZE_Y))

backgroundGameOver_surf = pygame.image.load('images/resizeBackgroundGameOver.png')
backgroundGameOver_rect = backgroundGameOver_surf.get_rect(bottomright=(BACKGROUND_SIZE_X,
                                                                        BACKGROUND_SIZE_Y))
gameOver_surf = pygame.image.load('images/gameOver.jpg')
gameOver_rect = gameOver_surf.get_rect(bottomright=(GAME_OVER_X, GAME_OVER_Y))

win_surf = pygame.image.load('images/win.png')
win_rect = win_surf.get_rect(bottomright=(GAME_OVER_X, GAME_OVER_Y))

coordinateOfFlags = []
coordinateOfBombs = []
field = []

for r in range(1, ROW + 1):
    row = []

    for c in range(1, COLUMN + 1):
        row.append(Cell(c * CELL_SIZE_X + OFFSET_FROM_EDGE,
                        r * CELL_SIZE_Y + OFFSET_FROM_EDGE))
        # print(row)
    field.append(row)

# print(field[0])
# print(field[0].index(cellSearchByCoordinate(520, 450)))
# field[0][8].isBomb = True

pygame.init()

while isOn:
    if isGameOver:
        drawGameOverBackgroundAndGameOver()

        events = pygame.event.get()

        for event in events:

            if event.type == pygame.QUIT:
                isOn = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    restartGame()
    # if isMenuOn:
    elif not isMenuOn:
        menu_surf = pygame.image.load('images/menu.png')
        menu_rect = menu_surf.get_rect(bottomright=(MAP_SIZE_X + OFFSET_FROM_EDGE, MAP_SIZE_Y + OFFSET_FROM_EDGE))
        sc.blit(menu_surf, menu_rect)

    else:

        sc.blit(background_surf, background_rect)

        for series in field:

            for cell in series:
                cell.drawCell()

        events = pygame.event.get()
        position = pygame.mouse.get_pos()
        # print(position)

        if OFFSET_FROM_EDGE <= position[0] < BACKGROUND_SIZE_X - OFFSET_FROM_EDGE and \
                OFFSET_FROM_EDGE <= position[1] < BACKGROUND_SIZE_Y - OFFSET_FROM_EDGE:
            cellSearchByCoordinate(*position).drawBrightCell()

        for event in events:

            if event.type == pygame.QUIT:
                isOn = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    restartGame()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.button)
                nucleus = cellSearchByCoordinate(*position)

                if type(nucleus) != Cell:
                    continue

                xCell, yCell = findLocationOfObject(nucleus)

                if event.button == 1:  # Левая кнопка мыши

                    if nucleus.mode == 2 or nucleus.mode == 3:

                        if nucleus.mode == 2:
                            coordinateOfFlags.remove((xCell, yCell))

                        nucleus.mode = 0

                    else:
                        if nucleus.isBomb:
                            for column, row in coordinateOfBombs:
                                nucleus = field[row][column]
                                nucleus.mode = 1
                                nucleus.drawCell()

                            pygame.display.update()
                            pygame.time.delay(700)
                            isGameOver = True

                        xCell, yCell = findLocationOfObject(nucleus)

                        if isFirstPress:
                            isFirstPress = False
                            generateBombs()

                        openCell(xCell, yCell)

                elif event.button == 2:  # Нажатие на колесико мыши

                    if nucleus.mode != 1:
                        nucleus.mode = 3

                elif event.button == 3:  # Правая кнопка мыши

                    if nucleus.mode != 1:
                        nucleus.mode = 2
                        coordinateOfFlags.append((xCell, yCell))

                        if len(coordinateOfFlags) == len(coordinateOfBombs):
                            # print(coordinateOfBombs, coordinateOfFlags, sep='\n')
                            isWin = True

                            for flag in coordinateOfFlags:

                                if flag not in coordinateOfBombs:
                                    isWin = False
                                    break

                            if isWin:
                                isGameOver = True

                nucleus.drawCell()

        # print(pygame.mouse.get_pos())

    pygame.display.update()

    clock.tick(FPS)

exit(0)
