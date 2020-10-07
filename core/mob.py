# mob.py:

import pygame

from . import utils

class Mob(pygame.Rect):
    pattern = [0,1,0,2]
    facings = { "south": 0, "north": 1, "east": 2, "west": 3 }

    def __init__(self, uid, name, spr_obj):
        self.uid = uid # simply so you can have multiple characters with the same name
        self.name = name
        self.sprite = spr_obj
        pygame.Rect.__init__(self, (0,0,self.sprite.w,self.sprite.h))

        self.scene = None   # contains info on the map and other mobs; collisions
        self.moving = False # 
        self.face = "south" # direction the mob is facing
        self.frame = 0      # for animation
        self.speed = 2      # pixel precision
        self.alive = True   # if True then rect collision check
        self.dying = False  # triggers the fading routine
        self.fading = False # trigger that's pulled and held
        self.opacity = 255 # need a solution since more than one mob can have the same Spriteset

    def spawn(self, scn_obj):
        if self.scene != scn_obj:
            self.scene = scn_obj
        	self.scene.live_mobs[self.uid] = self
        	# trigger a fade in event here?

    def update(self, signals, fc): pass
    def render(self, surface): pass
