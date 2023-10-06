import pygame, time, random

pygame.init()

screen = pygame.display.set_mode((1200,680))
pygame.display.set_caption("Dastan")

BACKGROUND = (40,40,40)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)

BOARD_THEMES = [((140, 51, 19), (230, 166, 68)),
                ((181, 136, 99), (240, 217, 181)),
                ((116, 148, 84), (236, 236, 212))]
BOARD1, BOARD2 = BOARD_THEMES[1]

clock = pygame.time.Clock()

play = True

ticker = 0

def drawBoard(position, size):
    x, y = position
    xjump, yjump = size[0]//6, size[1]//6
    for i in range(6):
        for j in range(6):
            if (i + j)%2:
                pygame.draw.rect(screen, BOARD1, ((x + i*xjump, y + j*yjump), (xjump, yjump)))
            else:
                pygame.draw.rect(screen, BOARD2, ((x + i*xjump, y + j*yjump), (xjump, yjump)))
    pygame.draw.rect(screen, WHITE, (position, size), 2)

def draw(color, x, y):
    pygame.draw.circle(screen, color, (x, y), 40, 0)

while play:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    drawBoard((50, 40), (600, 600))
    
    pygame.display.update()


pygame.quit()
