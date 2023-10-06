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
BOARD1, BOARD2 = BOARD_THEMES[2]

clock = pygame.time.Clock()

play = True

ticker = 0

def drawBoard():
    pygame.draw.rect(screen, WHITE, ((49, 39), (602, 602)))
    for i in range(6):
        for j in range(6):
            if i%2:
                if j%2:
                    pygame.draw.rect(screen, BOARD2, ((50 + i*100, 40 + j*100), (100, 100)))
                else:
                    pygame.draw.rect(screen, BOARD1, ((50 + i*100, 40 + j*100), (100, 100)))
            else:
                if j%2:
                    pygame.draw.rect(screen, BOARD1, ((50 + i*100, 40 + j*100), (100, 100)))
                else:
                    pygame.draw.rect(screen, BOARD2, ((50 + i*100, 40 + j*100), (100, 100)))

def draw(color, x, y):
    pygame.draw.circle(screen, color, (x, y), 40, 0)

while play:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    drawBoard()
    
    pygame.display.update()


pygame.quit()
