import pygame, time, random

BACKGROUND = (40,40,40)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)

class QueueButton:
    def __init__(self):
        ##### TODO ######
        pass


class Game:
    THEMES = [((140, 51, 19), (230, 166, 68)),
              ((181, 136, 99), (240, 217, 181)),
              ((116, 148, 84), (236, 236, 212))]

    def __init__(self, size = (1000, 600)):
        self.size = size
        self.board_size = (size[1], size[1])  # this will give a square board of y size
        self.queue_size = (size[0] - size[1], size[1])  # the remaining space left after board is taken
        self.queue_pos = (size[1], 0)
        self.theme = 0

    def draw(self) -> pygame.Surface:
        """Returns a surface contining the game drawn onto it"""
        canvas = pygame.Surface(self.size)
        canvas.blit(self.draw_board(), (0, 0))
        canvas.blit(self.draw_queue(), self.queue_pos)
        return canvas


    def draw_board(self) -> pygame.Surface:
        """Returns a surface containing the board"""
        canvas = pygame.Surface(self.board_size)
        x, y = self.board_size
        xjump, yjump = x//6, y//6
        c1, c2 = self.THEMES[self.theme]

        for i in range(6):
            for j in range(6):
                if (i + j)%2:
                    pygame.draw.rect(canvas, c1, ((i * xjump, j * yjump), (xjump, yjump)))
                else:
                    pygame.draw.rect(canvas, c2, ((i * xjump, j * yjump), (xjump, yjump)))
        pygame.draw.rect(canvas, WHITE, ((0, 0), self.board_size), 2)

        return canvas

    def draw_queue(self) -> pygame.Surface:
        """Returns a surface containing the queue buttons"""
        ######## TODO ##########
        canvas = pygame.Surface(self.queue_size)
        canvas.fill(BACKGROUND)
        return canvas

    def handle_click(self, position):
        """deals with what to do when it is clicked"""
        ######## TODO ##########
        pass
