
import sys

import pygame

from pyengine.system.display import PyEngineDisplay
from pyengine.system.renderer import PyEngineRenderer



class PyEngine:

    def __init__(self):
        
        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = False

        self.display = PyEngineDisplay()

        self.scene = None
        
        self.frame_rate = 60
        self.dt = 0



    def run(self):

        self.display._load_display()
        self.mainloop()

    

    def mainloop(self):

        self.running = True



        while self.running:

            self.dt = self.clock.tick(self.frame_rate) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.display.update_display()



        pygame.quit()
        sys.exit()