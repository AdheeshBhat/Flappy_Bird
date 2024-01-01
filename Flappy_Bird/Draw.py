import Setup
import Movement
import pygame
from pygame.locals import *
import random
import keyboard
import Key_Pressed
to_rotate = True
pole_boolean = False
game_started = False
score = 0
font = pygame.font.Font('Monsterrat.ttf', 40)
clock = pygame.time.Clock()
clock.tick(30)
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
MAX_COLUMN_HEIGHT = height - 200
MIN_COLUMN_HEIGHT = height - 600

bird_gui, screen, pole_gui, height, width, rotated_bird_gui, pole_list = Setup.setup()

#sets pole dimensions
class pole:
    def __init__(self):
        self.width = 500
        self.height = random.randint(MIN_COLUMN_HEIGHT, MAX_COLUMN_HEIGHT)
        self.position = random.randint(0,1)
        self.x = 100
        self.image = pygame.image.load("flappy_bird_pole_image.png")
        self.bit = 0

bird_x = -30
bird_y = 300
game_ended_bit = 0

width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

pygame.display.set_icon(bird_gui)

bird_gui, screen, pole_gui, height, width, rotated_bird_gui, pole_list = Setup.setup()

last_space_time = 0

while True:
    if game_started:
        bird_y += 8
    
    #loops over each event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        bird_y, last_space_time, to_rotate, pole_boolean, game_started, game_ended_bit = Key_Pressed.key_Pressed(event,
        bird_y, last_space_time, to_rotate, pole_boolean, game_started,
        game_ended_bit)

    screen.fill((255,255,255))
    #loops over pole list
    for i in range(len(pole_list)):
        #collisions for top pole
        if pole_list[i].position == 0:
            #bird_x - 50 is the right side of the bird
            if pole_list[i].x <= bird_x - 50 and pole_list[i].height >= bird_y:
                pole_boolean = False
                game_ended_bit = 1
        #bottom pole
        else:
            if pole_list[i].x <= bird_x - 50 and pole_list[i].height <= bird_y + 150:
                pole_boolean = False
                game_ended_bit = 1

        #scoreboard
        if pole_list[i].x <= bird_x - 50 and pole_list[i].bit == 0:
            score += 1
            pole_list[i].bit = 1
            
        #checks if poles go off screen and spawns new poles
        if pole_list[i].x <= -200:
            current_pole = pole()
            #flips the pole image if the pole is hanging from the top.
            if current_pole.position == 0:
                current_pole.image = pygame.transform.flip(current_pole.image, False, True)
            current_pole.x = width + 100
            pole_list[i] = current_pole

        #moves poles left
        if pole_boolean == True:
            pole_list[i].x -= 5
        #spawns poles in from the top
        if pole_list[i].position == 0:
            screen.blit(pole_list[i].image, (pole_list[i].x, 0))

        #spawns poles in from the bottom
        else:
            screen.blit(pole_list[i].image, (pole_list[i].x, pole_list[i].height))
    
        current_time = pygame.time.get_ticks()
        if current_time - last_space_time > 300:
         to_rotate = True
        
    text = font.render("Score: " + str(score), True,(0,0,0) , (31,127,229))
    screen.blit(text, (1340,10))

    #else:
    Movement.bird_gui_position(bird_gui, screen, bird_x, bird_y, to_rotate, rotated_bird_gui)
        
    pygame.display.update()
    clock.tick()

    