import pygame

pygame.init()

screen = pygame.display.set_mode((600,800))

pygame.draw.rect(screen, 0xFF0000, pygame.Rect(0,0,100,100))

exit = False

while not Exit:
    for event in pygame.event.get()
        if event.type == pygame.QUIT:
            Exit = True