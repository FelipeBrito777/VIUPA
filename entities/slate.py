from cmath import rect
from importlib import resources

import pygame
from pygame.locals import *
from healthy.config import cfg_item



class Slate:
    pygame.init()
    __size = [300, 200]
    __window = pygame.display.set_mode(__size)
    __black = pygame.color.Color('#000000')
    __magenta = pygame.color.Color('#5BF7E8')
    __font = pygame.font.Font(None, 40)
    __done = False

      

    def __init__(self):
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.__positionb = pygame.math.Vector2(0,0)     

        with resources.path(cfg_item('back','back_ground_pack'), cfg_item('back','back_ground_file')) as slate_image_path:
            self.__imageb = pygame.image.load(slate_image_path).convert_alpha()
            
        with resources.path(cfg_item('music','music_pack'), cfg_item('music','music_file')) as song_path:
             self.__song = pygame.mixer.music.load(song_path) 
             pygame.mixer.music.play()

        
             

    def render(self, surface_dest):
        surface_dest.blit(self.__imageb, self.__positionb.xy)
      

    def spinach(self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        asp = __position_mouse[0]
        bs = __position_mouse[1]
        for event in pygame.event.get():
            if asp > 0 and asp <= 209 and bs > 0 and bs <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Es una fuente de Calcio\nUna fuente de Hierro\ny Una fuente de proteínas vegetales\n""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)
                                    with resources.path(cfg_item('wow','wow_pack'), cfg_item('wow','wow_file')) as wow_path:
                                        self.__wow_sound = pygame.mixer.music.load(wow_path)
                                        pygame.mixer.music.play()  

     
    def soja_beans(self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        asb = __position_mouse[0]
        bsb = __position_mouse[1]
        for event in pygame.event.get():
            if asb > 214 and asb <= 426 and bsb > 0 and bsb <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro\ny Buena fuente de proteínas vegetales\n""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)


    def pumkin_seeds (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        aps = __position_mouse[0]
        bps = __position_mouse[1]
        for event in pygame.event.get():
            if aps > 435 and aps <= 635 and bps > 0 and bps <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000) 

    def almonds (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        #print(__position_mouse)
        aa = __position_mouse[0]
        ba = __position_mouse[1]
        for event in pygame.event.get():
            if aa > 655 and aa <= 855 and ba > 0 and ba <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Es una fuente de Calcio\nUna fuente de Hierro\ny Una fuente de proteínas vegetales\n""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)
                                    with resources.path(cfg_item('wow','wow_pack'), cfg_item('wow','wow_file')) as wow_path:
                                        self.__wow_sound = pygame.mixer.music.load(wow_path)
                                        pygame.mixer.music.play()  

    def cabbage (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ac = __position_mouse[0]
        bc = __position_mouse[1]
        for event in pygame.event.get():
            if ac > 855 and ac <= 1055 and bc > 0 and bc <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)


    def kale (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ak = __position_mouse[0]
        bk = __position_mouse[1]
        for event in pygame.event.get():
            if ak > 1065 and ak <= 1275 and bk > 0 and bk <= 156:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def quinoa (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        aq = __position_mouse[0]
        bq = __position_mouse[1]
        for event in pygame.event.get():
            if aq > 0 and aq <= 209 and bq > 158 and bq <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro\ny Buena fuente de proteínas vegetales\n""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def wheat_germ (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        awg = __position_mouse[0]
        bwg = __position_mouse[1]
        for event in pygame.event.get():
            if awg > 214 and awg <= 426 and bwg > 158 and bwg <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def chard (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ach = __position_mouse[0]
        bch = __position_mouse[1]
        for event in pygame.event.get():
            if ach > 435 and ach <= 635 and bch > 158 and bch <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000) 

    def chia_seeds (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        acs = __position_mouse[0]
        bcs = __position_mouse[1]
        for event in pygame.event.get():
            if acs > 655 and acs <= 855 and bcs > 158 and bcs <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio \n y Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)  

    def oat (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ao = __position_mouse[0]
        bo = __position_mouse[1]
        for event in pygame.event.get():
            if ao > 855 and ao <= 1055 and bo > 158 and bo <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Proteínas\n y de Hierro""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000) 

    def beans (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ab = __position_mouse[0]
        bb = __position_mouse[1]
        for event in pygame.event.get():
            if ab > 1065 and ab <= 1275 and bb > 158 and bb <= 310:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Proteínas\n y de Hierro""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000) 

    def rice (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ar = __position_mouse[0]
        br = __position_mouse[1]
        for event in pygame.event.get():
            if ar > 0 and ar <= 209 and br > 312 and br <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000) 

    def orange (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ao = __position_mouse[0]
        bo = __position_mouse[1]
        for event in pygame.event.get():
            if ao > 214 and ao <= 426 and bo > 312 and bo <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def lentils (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        al = __position_mouse[0]
        bl = __position_mouse[1]
        for event in pygame.event.get():
            if al > 435 and al <= 635 and bl > 312 and bl <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro\ y buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)  
    
    def tofu(self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        at = __position_mouse[0]
        bt = __position_mouse[1]
        for event in pygame.event.get():
            if at > 655 and at <= 855 and bt > 312 and bt <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Es una fuente de Calcio\nUna fuente de Hierro\ny Una fuente de proteínas vegetales\n""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)
                                    with resources.path(cfg_item('wow','wow_pack'), cfg_item('wow','wow_file')) as wow_path:
                                        self.__wow_sound = pygame.mixer.music.load(wow_path)
                                        pygame.mixer.music.play()  

    def broccoli (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ab = __position_mouse[0]
        bb = __position_mouse[1]
        for event in pygame.event.get():
            if ab > 855 and ab <= 1055 and bb > 312 and bb <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)  

    def dried_figs (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ad = __position_mouse[0]
        bd = __position_mouse[1]
        for event in pygame.event.get():
            if ad > 1065 and ad <= 1275 and bd > 312 and bd <= 465:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def pack_choi (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        apc = __position_mouse[0]
        bpc = __position_mouse[1]
        for event in pygame.event.get():
            if apc > 0 and apc <= 209 and bpc > 470 and bpc <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def fortified_vegetable_beverages (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        afvb = __position_mouse[0]
        bfvb = __position_mouse[1]
        for event in pygame.event.get():
            if afvb > 214 and afvb <= 426 and bfvb > 470 and bfvb <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)
        
    def cauiflower (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        aca = __position_mouse[0]
        bca = __position_mouse[1]
        for event in pygame.event.get():
            if aca > 435 and aca <= 635 and bca > 470 and bca <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio\n y Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def peanut (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        ap = __position_mouse[0]
        bp = __position_mouse[1]
        for event in pygame.event.get():
            if ap > 655 and ap <= 855 and bp > 470 and bp <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Hierro\n y Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def amaranth (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        aa = __position_mouse[0]
        ba = __position_mouse[1]
        for event in pygame.event.get():
            if aa > 1065 and aa <= 1275 and ba > 470 and ba <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio\n y Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)

    def sesame_seeds (self, __position_mouse):
        __position_mouse = pygame.mouse.get_pos()
        asse = __position_mouse[0]
        bsse = __position_mouse[1]
        for event in pygame.event.get():
            if asse > 855 and asse <= 1055 and bsse > 470 and bsse <= 620:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_press = pygame.mouse.get_pressed()
                    if mouse_press[0]:
                        with resources.path(cfg_item('metal','metal_pack'), cfg_item('metal','metal_file')) as metal_path:
                                self.__metal_sound = pygame.mixer.music.load(metal_path)
                                pygame.mixer.music.play() 
                        text = Slate.__font.render("""Buena fuente de Calcio\n y Buena fuente de Proteínas""", False, Slate.__black)
                        while not Slate.__done:
                            Slate.__window.fill(Slate.__magenta)
                            Slate.__window.blit(text, (0,0))
                            pygame.display.flip()
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    Slate.__done = True 
                                elif event.type == pygame.MOUSEBUTTONUP:
                                    pygame.time.wait(3000)
    
      
 
    def quit(self):
        pass