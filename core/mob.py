# mob.py:

import pygame

from . import utils

class Mob(pygame.Rect):
    pattern = [0,1,0,2]
    facings = { "south": 0, "north": 1, "east": 2, "west": 3 }

    def __init__(self, uid, name, spr_obj, grp=None, script=None):
        self.uid = uid # simply so you can have multiple characters with the same name
        self.name = name
        self.sprite = spr_obj
        pygame.Rect.__init__(self, (0,0,self.sprite.w,self.sprite.h))
        self.alive = True   # if True then rect collision check
        self.dying = False  # triggers the fading routine
        self.fading = False # trigger that's pulled and held
        self.moving = False # 
        self.scene = None   # contains info on the map and other mobs; collisions
        self.face = "south" # direction the mob is facing
        self.frame = 0      # for animation
        self.opacity = 255  # need a solution since more than one mob can have the same Spriteset
        self.spawn_c = 0
        self.spawn_r = 0
        self.speed = 2      # pixel precision
        self.script = script
        if grp and type(grp).__name__ == 'list':
            self.grp = grp
            grp[self.uid] = self
            
    def spawn(self):
        self.place(self.spawn_c, self.spawn_r)
        self.scene.live_mobs[self.uid] = self
        # trigger a fade in event here?
        	
    def place(self, col, row):
        self.x = col * self.scene_obj.tile_w + (self.scene_obj.tile_w - self.w) / 2
        self.y = row * self.scene_obj.tile_h + (self.scene_obj.tile_h - self.h) - 4

    def update(self, signals, fc):
        if self.script: self.script(self)
    def render(self, surface): pass
