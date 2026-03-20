import pygame
from settings import *
from entity import Entity
from support import *

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # graphics set up
        self.import_graphics(monster_name)
        self.image = pygame.Surface((64, 64))
        self.rect = self.image.get_rect(topleft = pos)

    def import_graphics(self, name):
        self.animations = {'idle':[], 'move':[], 'attack':[]}
        main_path = f'graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)