import Setup
import pygame
import keyboard
import Movement

def key_Pressed(event, bird_y, last_space_time, to_rotate, pole_boolean, game_started, game_ended_bit):
    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.MOUSEBUTTONDOWN or event.key == pygame.K_SPACE:
            if game_ended_bit == 0:
                last_space_time = pygame.time.get_ticks()
                pygame.display.update()
                bird_y = Movement.bird_movement(bird_y)
                to_rotate = False
                pole_boolean = True
                game_started = True
            
    return bird_y, last_space_time, to_rotate, pole_boolean, game_started, game_ended_bit