import pygame
from pygame.locals import *
import sys
from random import randint, seed

pygame.init()

size = width, height = 1920, 1080
#size = width, height = 800, 600
screen = pygame.display.set_mode(size,FULLSCREEN)
#screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pingu Pongu")
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
CYAN  = (  0, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
MAGENTA= (255,   0, 255)

while True:
    clock.tick(20)
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #screen.fill(BLACK)
    screen.fill((0,32,0))

    pygame.display.flip()
