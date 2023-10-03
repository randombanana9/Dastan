import pygame, time, random

pygame.init()

screen = pygame.display.set_mode((1200,680))
pygame.display.set_caption("Dastan")

BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()

play = True

ticker = 0

def drawBoard():
    for i in range(6):
        for j in range(6):
            if i%2:
                if j%2:
                    pygame.draw.rect(screen, WHITE, ((50 + i*100, 40 + j*100), (100, 100)))
                else:
                    pygame.draw.rect(screen, GREEN, ((50 + i*100, 40 + j*100), (100, 100)))
            else:
                if j%2:
                    pygame.draw.rect(screen, GREEN, ((50 + i*100, 40 + j*100), (100, 100)))
                else:
                    pygame.draw.rect(screen, WHITE, ((50 + i*100, 40 + j*100), (100, 100)))

def draw(color, x, y):
    pygame.draw.circle(screen, color, (x, y), 40, 0)

while play:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    drawBoard()
    
    pygame.display.update()


pygame.quit()
