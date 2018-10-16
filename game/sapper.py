import pygame
from settings import *
from cell import Cell


def cellSearchByCoordinate(x, y):
    for line in field:

        for nucl in line:

            if nucl.x - CELL_SIZE_X <= x <= nucl.x and nucl.y - CELL_SIZE_Y <= y <= nucl.y:
                return nucl


def restartGame():
    for line in field:

        for nucl in line:

            nucl.isBomb = False
            nucl.mode = 0
            nucl.numberOfBombNear = 0
            nucl.nameImage = 'closed_cell.png'


pygame.init()

isOn = True
isMenuOn = True

clock = pygame.time.Clock()
sc = pygame.display.set_mode((MAP_SIZE_X + OFFSET_FROM_EDGE * 2, MAP_SIZE_Y + OFFSET_FROM_EDGE * 2))

pygame.display.set_caption('Сапер')
# map_surf = pygame.image.load('map.png')
# map_rect = map_surf.get_rect(bottomright=(MAP_SIZE_X + OFFSET_FROM_EDGE, MAP_SIZE_Y + OFFSET_FROM_EDGE))
#
# sc.blit(map_surf, map_rect)


field = []

for r in range(1, ROW + 1):
    row = []

    for c in range(1, COLUMN + 1):
        row.append(Cell(c * CELL_SIZE_X + OFFSET_FROM_EDGE,
                        r * CELL_SIZE_Y + OFFSET_FROM_EDGE))
        # print(row)
    field.append(row)

f = field.copy()

while isOn:
    # if isMenuOn:
    if not isMenuOn:
        menu_surf = pygame.image.load('image/menu.png')
        menu_rect = menu_surf.get_rect(bottomright=(MAP_SIZE_X + OFFSET_FROM_EDGE, MAP_SIZE_Y + OFFSET_FROM_EDGE))
        sc.blit(menu_surf, menu_rect)

    else:

        for series in field:

            for cell in series:
                cell.drawCell()

        events = pygame.event.get()
        position = pygame.mouse.get_pos()

        if OFFSET_FROM_EDGE <= position[0] < MAP_SIZE_X + OFFSET_FROM_EDGE and\
                OFFSET_FROM_EDGE <= position[1] < MAP_SIZE_Y + OFFSET_FROM_EDGE:

            cellSearchByCoordinate(*position).drawBrightCell()

        for event in events:

            if event.type == pygame.QUIT:
                isOn = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_r:
                    restartGame()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                nucleus = cellSearchByCoordinate(*position)

                if event.button == 1:  # Левая кнопка мыши
                    if nucleus.mode == 2 or nucleus.mode == 3:
                        nucleus.mode = 0

                    else:
                        nucleus.mode = 1

                    nucleus.drawCell()

                elif event.button == 2:  # Нажатие на колесико мыши
                    if nucleus.mode != 1:
                        nucleus.mode = 3

                    nucleus.drawCell()

                elif event.button == 3:  # Правая кнопка мыши
                    if nucleus.mode != 1:
                        nucleus.mode = 2

                nucleus.drawCell()

        # print(pygame.mouse.get_pos())

    pygame.display.update()

    clock.tick(FPS)

exit(0)
