from importlib import resources

import pygame

from healthy.config import cfg_item


class Boy:

    def __init__(self):
        
        with resources.path(cfg_item('little','image_pack'), cfg_item('little','image_file')) as boy_image_path:
            self.__image = pygame.image.load(boy_image_path).convert_alpha()

        self.__position = pygame.math.Vector2(cfg_item('game','screen_size')[0]/1.2, cfg_item('game','screen_size')[1]/1.5)

        self.__moving_right = False
        self.__moving_left = False
        self.__moving_up = False
        self.__moving_down = False

    def handle_input(self, key, is_pressed):
        if key == pygame.K_UP:
            pass
        if key == pygame.K_DOWN:
            pass
        if key == pygame.K_LEFT:
            self.__moving_left = is_pressed
        if key == pygame.K_RIGHT:
            self.__moving_right = is_pressed

    def update(self, delta_time):
        movement = pygame.math.Vector2(0.0, 0.0)
        if self.__moving_up:
            pass
        if self.__moving_down:
            pass
        if self.__moving_left:
            movement.x -= cfg_item('healthy', 'speed')
        if self.__moving_right:
            movement.x += cfg_item('healthy', 'speed')

        self.__position += movement * delta_time

   
    def render(self, surface_dest):
        #print("entra a render de Boy" )
        surface_dest.blit(self.__image, self.__position.xy)

    def quit(self):
        pass