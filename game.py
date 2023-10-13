import pygame, time, random

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

BACKGROUND = (40,40,40)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)

RY = (15, 150, 15)
CH = (50, 50, 255)
FA = (200, 25, 25)
CU = (190, 5, 190)
JA = (255, 255, 0)

moveColours = {"Ryott": RY, "Chowkidar": CH, "Faujdar": FA, "Cuirassier": CU, "Jazair": JA}

class QueueButton:
    def __init__(self, move, cost = 0, size = (100,30)):
        self.move = move
        self.cost = cost
        self.size = size
        self.text_colour = WHITE
    
    def draw(self, selected = False):
        font = pygame.font.SysFont('Comic Sans MS', int(self.size[1]*0.8))

        canvas = pygame.Surface(self.size)
        canvas.fill(BACKGROUND)
        pygame.draw.rect(canvas, moveColours[self.move], ((0, 0), self.size), border_radius = 5)
        canvas.blit(font.render(self.move, True, self.text_colour), (0, 0))
        return canvas



class Game:
    THEMES = [((140, 51, 19), (230, 166, 68)),
              ((181, 136, 99), (240, 217, 181)),
              ((116, 148, 84), (236, 236, 212))]

    def __init__(self, size = (1200, 700)):
        self.size = size # Size of the game canvas
        self.board_size = (size[1]*5/7)+(6-(size[1]*5/7)%6)+2  # this will give a square board of 5/7th of the y size (rounded up to the neares multiple of 6)
        self.queue_size = (size[0] - self.board_size, size[1])  # the remaining space left after board is taken
        #The next line is prety simple so if you dont understand it its on you
        self.queue_pos = ((2*(self.size[1] - self.board_size)//2.5-1) + self.board_size , (self.size[1] - self.board_size)//2-1 + self.board_size//3)  
        self.theme = 0  # Current theme

        ####temp#####
        self.queue1 = [QueueButton(i) for i in moveColours.keys()]

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
        for index, button in enumerate(self.queue1):
            canvas.blit(button.draw(), ((index)*110, 0))
        return canvas

    def handle_click(self, position):
        """deals with what to do when it is clicked"""
        ######## TODO ##########
        pass
