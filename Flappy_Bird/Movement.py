import Setup
import pygame
import keyboard
from pygame.locals import *
def bird_movement(bird_y):
    bird_y -= 200
    return bird_y

def bird_gui_position(bird_gui, screen, bird_x, bird_y, to_rotate, rotated_bird_gui):
    if to_rotate:
        screen.blit(bird_gui, (bird_x, bird_y))
    else:
        screen.blit(rotated_bird_gui, (bird_x, bird_y))