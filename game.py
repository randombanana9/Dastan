import pygame, time, random

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

SCREEN_SIZE = (1200, 700)

BACKGROUND = (40, 40, 40)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RY = (15, 150, 15)
CH = (50, 50, 255)
FA = (200, 25, 25)
CU = (190, 5, 190)
JA = (255, 255, 0)

moveColours = {"Ryott": RY, "Chowkidar": CH, "Faujdar": FA, "Cuirassier": CU, "Jazair": JA}

class QueueButton:
    def __init__(self, move, position, cost = 0, size = (SCREEN_SIZE[0]//12,SCREEN_SIZE[1]//70 * 3)):
        self.move = move
        self.position = position   # The buttons position on the queue canvas
        self.cost = cost
        self.size = size
        self.text_colour = WHITE
    
    def draw(self, selected = False) -> pygame.Surface:
        """Returns the surface containing the button drawn on"""
        font = pygame.font.SysFont('Trebuchet MS', int(self.size[1]*0.72))

        canvas = pygame.Surface(self.size)
        canvas.fill(BACKGROUND)
        pygame.draw.rect(canvas, moveColours[self.move], ((0, 0), self.size), border_radius = 5)
        txtW, txtH = font.size(self.move)
        for i in range(4):
            if i%2:
                if (i//2)%2:
                    canvas.blit(font.render(self.move, True, BLACK), ((self.size[0]-txtW)//2+1, (self.size[1]-txtH)//2+1))
                else:
                    canvas.blit(font.render(self.move, True, BLACK), ((self.size[0]-txtW)//2+1, (self.size[1]-txtH)//2-1))
            else:
                if (i//2)%2:
                    canvas.blit(font.render(self.move, True, BLACK), ((self.size[0]-txtW)//2-1, (self.size[1]-txtH)//2+1))
                else:
                    canvas.blit(font.render(self.move, True, BLACK), ((self.size[0]-txtW)//2-1, (self.size[1]-txtH)//2-1))
        canvas.blit(font.render(self.move, True, self.text_colour), ((self.size[0]-txtW)//2, (self.size[1]-txtH)//2))
        #########TODO#########
        # -Change coulour if selected
        # -Add outline
        return canvas
    
    def contains(self, position) -> bool:
        """Returns True if a given position is withthin the buttons position on the board"""
        x, y = position
        px, py = self.position
        sx, sy = self.size
        if px <= x <= px + sx and py <= y <= py + sy:
            return True
        return False



class Game:
    THEMES = [((140, 51, 19), (230, 166, 68)),
              ((181, 136, 99), (240, 217, 181)),
              ((116, 148, 84), (236, 236, 212))]

    def __init__(self, size = SCREEN_SIZE):
        self.size = size # Size of the game canvas
        self.board_size = (size[1]*5/7)+(6-(size[1]*5/7)%6)+2  # this will give a square board of 5/7th of the y size (rounded up to the neares multiple of 6)
        self.board_position = ((self.size[1] - self.board_size)//2.5-1, (self.size[1] - self.board_size)//2-1)
        self.queue_size = (size[0] - self.board_size - self.board_position[0]-2, self.board_size)  # the remaining space left after board is taken   -      NEEDS TO BE FIXED
        #The next line is prety simple so if you dont understand it its on you
        #self.queue_pos = ((2*(self.size[1] - self.board_size)//2.5-1) + self.board_size , (self.size[1] - self.board_size)//2-1 + self.board_size//3)  
        self.queue_pos = ((self.size[1] - self.board_size)//2.5 + self.board_size + 1, (self.size[1] - self.board_size)//2-1)
        self.theme = 0  # Current theme
        ####temp#####
        self.queue1 = [QueueButton(i, (SCREEN_SIZE[0]//11 * index, self.queue_size[1]//3)) for index, i in enumerate(moveColours.keys())]

    def draw(self) -> pygame.Surface:
        """Returns a surface contining the game drawn onto it"""
        canvas = pygame.Surface(self.size)
        canvas.fill(BACKGROUND)
        canvas.blit(self.draw_board(), self.board_position)
        canvas.blit(self.draw_queue(), self.queue_pos)
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

    def draw_queue(self) -> pygame.Surface:
        """Returns a surface containing the queue buttons"""
        ######## TODO ##########
        canvas = pygame.Surface(self.queue_size)
        canvas.fill(BACKGROUND)
        for button in self.queue1:
            canvas.blit(button.draw(), button.position)
        
        return canvas

    def handle_click(self, position):
        """deals with what to do when it is clicked"""
        x, y = position
        bx, by = self.board_position[0] + 1, self.board_position[1] + 1   # +1 so that border is avoided
        bs = self.board_size - 2 # -2 to avoid border
        if bx <= x <= bx+bs and by <= y <= by+bs:
            square_size = bs // 6
            square_x = (x-bx) // square_size
            square_y = (y-by) // square_size
            print(f"Square ({square_x}, {square_y}) clicked!")
        else:
            qx, qy = self.queue_pos
            relative_pos = (x-qx, y-qy)
            for button in self.queue1:
                if button.contains(relative_pos):
                    print(f"Queue Button \"{button.move}\" pressed!")

        ######## TODO ##########
        # -Fix else condition when queue size fixed
        # -Fix queue when it is changed
        pass
