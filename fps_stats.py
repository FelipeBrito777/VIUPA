from importlib import resources

import pygame

from healthy.config import cfg_item

class FPSStats:

    def __init__(self):
        with resources.path(cfg_item('game', 'font', 'pack'), cfg_item('game', 'font', 'file')) as font_path:
            self.__font = pygame.font.Font(font_path, cfg_item('game', 'font', 'size'))

        self.__update_time = 0
        self.__render_fps = 0
        self.__update_fps = 0
        self.__calc_fps_surface()

    def update(self, delta_time):
        self.__update_fps += 1
        self.__update_time += delta_time

        if self.__update_time >= cfg_item('timing', 'max_time_update'):
            self.__calc_fps_surface()

            self.__update_time -= cfg_item('timing', 'max_time_update')
            self.__render_fps = 0
            self.__update_fps = 0

    def render(self, surface_dest):
        self.__render_fps += 1
        surface_dest.blit(self.__fps_surface, cfg_item('stats', 'position'))

    def __calc_fps_surface(self):
        self.__fps_surface = self.__font.render(f"Update {self.__update_fps} fps, Render {self.__render_fps} fps", True, cfg_item('stats', 'foreground_color'), None)