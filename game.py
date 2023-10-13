import pygame, time, random

BACKGROUND = (40,40,40)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)

RY = (15, 150, 15)
CH = (50, 50, 255)
FA = (200, 25, 25)
CU = (190, 5, 190)
JA = (255, 255, 0)

moveColors = {"Ryott": RY, "Chowkidar": CH, "Faujdar": FA, "Cuirassier": CU, "Jazair": JA}

class QueueButton:
    def __init__(self, move, position = 0, cost = 0, size = (100,30)):
        self.move = move
        self.position = position
        self.cost = cost
        self.size = size
        self.color = moveColors[move]


class Game:
    THEMES = [((140, 51, 19), (230, 166, 68)),
              ((181, 136, 99), (240, 217, 181)),
              ((116, 148, 84), (236, 236, 212))]

    def __init__(self, size = (1200, 700)):
        self.size = size
        self.board_size = (size[1]*5/7)+(6-(size[1]*5/7)%6)+2  # this will give a square board of y size
        self.queue_size = (size[0] - self.board_size, size[1])  # the remaining space left after board is taken
        self.queue_pos = (size[1], 0) 
        self.theme = 0

    def draw(self) -> pygame.Surface:
        """Returns a surface contining the game drawn onto it"""
        canvas = pygame.Surface(self.size)
        canvas.fill(BACKGROUND)
        canvas.blit(self.draw_board(), ((self.size[1] - self.board_size)//2.5-1, (self.size[1] - self.board_size)//2-1))
        canvas.blit(self.draw_queue(None), self.queue_pos)
        return canvas


    def draw_board(self) -> pygame.Surface:
        """Returns a surface containing the board"""
        canvas = pygame.Surface((self.board_size, self.board_size))
        x = y = self.board_size-2
        xjump, yjump = x//6, y//6
        c1, c2 = self.THEMES[self.theme]

        for i in range(6):
            for j in range(6):
                if (i + j)%2:
                    pygame.draw.rect(canvas, c1, ((1+i * xjump, 1+j * yjump), (xjump, yjump)))
                else:
                    pygame.draw.rect(canvas, c2, ((1+i * xjump, 1+j * yjump), (xjump, yjump)))
        pygame.draw.rect(canvas, WHITE, ((0, 0), (self.board_size, self.board_size)), 2)

        return canvas

    def draw_queue(self, queue) -> pygame.Surface:
        """Returns a surface containing the queue buttons"""
        ######## TODO ##########
        canvas = pygame.Surface(self.queue_size)
        canvas.fill(BACKGROUND)
        return canvas

    def handle_click(self, position):
        """deals with what to do when it is clicked"""
        ######## TODO ##########
        pass
