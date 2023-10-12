import pygame
import game

BACKGROUND = (40,40,40)

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((1200,680))
    pygame.display.set_caption("Dastan")
    
    dastan = game.Game()

    clock = pygame.time.Clock()

    play = True

    while play:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

        screen.blit(dastan.draw(), (49, 39)) 
        pygame.display.update()


    pygame.quit()


