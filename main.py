import pygame, time, random

pygame.init()

screen = pygame.display.set_mode((1200,680))
pygame.display.set_caption("Dastan")

BACKGROUND = (40,40,40)
RED = (255,0,0)
YELLOW = (255,255,0)
BOARD1 = (161, 116, 79)
BOARD2 = (222, 221, 170)
WHITE = (255, 255, 255)

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
