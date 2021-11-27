import pygame
import os

from pygame import display
pygame.font.init()

pygame.mixer.init()

# init display params
WIDTH, HEIGHT = 1250, 900
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) # display
pygame.display.set_caption("WorldBlocks")     # title
