
import pygame



class Scene:

    def __init__(self):
        
        self.scene_objects = {}

    

    def register_game_object(self, game_object:object, id:str):
        
        self.scene_objects[id] = game_object



    def get_scene_objects(self):

        return self.scene_objects



    def execute(self):

        for object in self.scene_objects:

            object.process()