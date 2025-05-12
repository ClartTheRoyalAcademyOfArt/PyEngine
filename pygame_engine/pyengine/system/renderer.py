
import pygame



class PyEngineRenderer:

    def __init__(self, display):
        
        self.display = display
        self.draw_queue = []
    


    def draw(self, surface:pygame.Surface, position:tuple, z_layer:int=0):

        self.draw_queue.append((z_layer, surface, position))

    

    def render(self):

        self.display.clear_display()

        for _, surface, pos in sorted(self.draw_queue, key=lambda x: x[0]):
            self.display.DISPLAY.blit(surface, pos)

        self.display.update_display()
        self.draw_queue.clear()