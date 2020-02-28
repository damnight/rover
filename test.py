import pygame
keys = pygame.key.get_pressed()

if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]:
    print('it works')