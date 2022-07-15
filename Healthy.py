import pygame

from healthy.fps_stats import FPSStats
from healthy.config import cfg_item
from healthy.entities.boy import Boy
from healthy.entities.slate import Slate


class Game:
    
    def __init__(self):
        
        pygame.init()

            
        self.__screen = pygame.display.set_mode(cfg_item('game','screen_size'), pygame.RESIZABLE,32)
        pygame.display.set_caption(cfg_item('game','caption'))
        
        self.__fps_stats = FPSStats()
        self.__kid = Boy()
        self.__slate = Slate()
       
        print("Comenzamos el juego")

                
    def run(self):
        self.__running=True

        last_time = pygame.time.get_ticks()
        time_since_last_update = 0
        time_per_frame = 1000.0 / cfg_item('timing', 'fps')
        while self.__running:
            delta_time, last_time = self.__calc_delta_time(last_time)
            time_since_last_update += delta_time
            while time_since_last_update > time_per_frame:
                time_since_last_update -= time_per_frame

                self.__handle_input()
                self.__update(time_per_frame)

            self.__render()

        self.__quit()

    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False
                else:
                    self.__kid.handle_input(event.key, True)
            if event.type == pygame.KEYUP:
                self.__kid.handle_input(event.key, False)

    def __update(self,delta_time):
        self.__fps_stats.update(delta_time)
        #self.__slate.update(delta_time)
        self.__kid.update(delta_time)
        
    def __render(self):
     
        self.__fps_stats.render(self.__screen)
        self.__slate.render(self.__screen)
        self.__slate.spinach(self.__screen)
        self.__slate.soja_beans(self.__screen)
        self.__slate.pumkin_seeds(self.__screen)
        self.__slate.almonds(self.__screen)
        self.__slate.cabbage(self.__screen)
        self.__slate.kale(self.__screen)
        self.__slate.quinoa(self.__screen)
        self.__slate.wheat_germ(self.__screen)
        self.__slate.chard(self.__screen)
        self.__slate.chia_seeds(self.__screen)
        self.__slate.oat(self.__screen)
        self.__slate.beans(self.__screen)
        self.__slate.rice(self.__screen)
        self.__slate.orange(self.__screen)
        self.__slate.lentils(self.__screen)
        self.__slate.tofu(self.__screen)
        self.__slate.broccoli(self.__screen)
        self.__slate.dried_figs(self.__screen)
        self.__slate.pack_choi(self.__screen)
        self.__slate.fortified_vegetable_beverages(self.__screen)
        self.__slate.cauiflower(self.__screen)
        self.__slate.peanut(self.__screen)
        self.__slate.amaranth(self.__screen)
        self.__slate.sesame_seeds(self.__screen)
        self.__kid.render(self.__screen)

        pygame.display.update()


    def __quit(self):
        self.__slate.quit()
        self.__kid.quit()
        pygame.quit() 

    def __calc_delta_time(self, last_time):
        current_time = pygame.time.get_ticks()
        delta = current_time - last_time
        return delta, current_time         
       