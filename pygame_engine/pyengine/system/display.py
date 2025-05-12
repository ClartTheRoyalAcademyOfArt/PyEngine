
import pygame



class PyEngineDisplay:

    def __init__(self):
        
        self.resolution = (1280, 720)
        self.flags = 0
        self.fill_color = (20, 20, 20)
        self.caption = "PyEngine"

        self.DISPLAY = None



    def configure_display(self, resolution:tuple=None, flags:int=None, fill_color:tuple=None, caption:str=None):

        if resolution is not None:
            self.resolution = resolution
        if flags is not None:
            self.flags = flags
        if fill_color is not None:
            self.fill_color = fill_color
        if caption is not None:
            self.caption = caption
    


    def _load_display(self):

        pygame.display.init()

        self.DISPLAY = pygame.display.set_mode(self.resolution, self.flags)
        pygame.display.set_caption(self.caption)
        self.clear_display()


    
    def reload_display(self):

        self.DISPLAY = pygame.display.set_mode(self.resolution, self.flags)
        pygame.display.set_caption(self.caption)
        self.clear_display()
    

    
    def clear_display(self):

        self.DISPLAY.fill(self.fill_color)

    

    def update_display(self):

        pygame.display.update()


    def get_display(self):

        return self.DISPLAY