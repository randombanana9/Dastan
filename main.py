import pygame, time, random

pygame.init()

screen = pygame.display.set_mode((1200,675))
pygame.display.set_caption("Dastan")

BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()

play = True

ticker = 0

def draw(color, x, y):
    pygame.draw.circle(screen, color, (x, y), 40, 0)

while play:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    pygame.display.update()


pygame.quit()
