import pygame


class WrongMode(Exception):
    pass


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.isBomb = False
        self.mode = 0  # 0 - close; 1 - open; 2 - flag; 3 - question
        self.numberOfBombNear = 0
        self.nameImage = 'closed_cell.png'
        self.isCheck = False

    def __str__(self):
        return '(' + ' '.join([str(self.x), str(self.y),
                               str(self.isBomb), str(self.mode),
                               str(self.numberOfBombNear), str(self.numberOfBombNear), self.nameImage, str(self.isCheck)
                               ]) + ')'

    def drawCell(self):
        from __main__ import sc

        if not self.mode:
            self.nameImage = 'closed_cell.png'

        elif self.isBomb and self.mode == 1:
            self.nameImage = 'bomb.png'

        elif self.mode == 1:
            self.nameImage = str(self.numberOfBombNear) + '.png'

        elif self.mode == 2:
            self.nameImage = 'labeled_cell.png'

        elif self.mode == 3:
            self.nameImage = 'cell_in_question.png'

        else:
            raise WrongMode('check cell.py')

        cell_surf = pygame.image.load('images/' + self.nameImage)
        cell_rect = cell_surf.get_rect(bottomright=(self.x, self.y))

        sc.blit(cell_surf, cell_rect)

    def drawBrightCell(self):
        from __main__ import sc

        bright_cell_surf = pygame.image.load('images/bright_' + self.nameImage)
        bright_cell_rect = bright_cell_surf.get_rect(bottomright=(self.x, self.y))

        sc.blit(bright_cell_surf, bright_cell_rect)
