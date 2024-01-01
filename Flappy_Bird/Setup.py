import pygame 
from pygame.locals import *
pygame.init()
import keyboard
import random
global MAX_COLUMN_HEIGHT
global MIN_COLUMN_HEIGHT

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
MAX_COLUMN_HEIGHT = height - 200
MIN_COLUMN_HEIGHT = height - 600

#sets pole dimensions
class pole:
    def __init__(self):
        self.width = 500
        self.height = random.randint(MIN_COLUMN_HEIGHT, MAX_COLUMN_HEIGHT)
        self.position = random.randint(0,1)
        self.x = 100
        self.image = pygame.image.load("flappy_bird_pole_image.png")
        self.bit = 0

def setup():
    bird_gui = pygame.image.load("flappy_bird_image.png")
    pole_gui = pygame.image.load("flappy_bird_pole_image.png")
    rotated_bird_gui = pygame.image.load("flappy_bird_image.png")
    screen = pygame.display.set_mode((width, height - 50))
    
    screen.fill((31, 133, 222))
    bird_gui = pygame.transform.smoothscale(bird_gui, (200,200))
    rotated_bird_gui = pygame.transform.smoothscale(rotated_bird_gui, (200,200))
    rotated_bird_gui = pygame.transform.rotate(rotated_bird_gui, 45)

    #This function puts the bird image on the screen.


    pole_list = []
    pivot = 400
    # loops over pole list 3 times
    for i in range(4):
        current_pole = pole()
        if current_pole.position == 0:
            current_pole.image = pygame.transform.flip(current_pole.image, False, True)
        current_pole.x = 400 + pivot* i
        
        pole_list.append(current_pole)

    return bird_gui, screen, pole_gui, height, width, rotated_bird_gui, pole_list

