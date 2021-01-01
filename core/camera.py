# camera.py:

import os

import pygame

from . import scene
from . import filepaths

class Camera(pygame.Rect): # legacy, modified;
    def __init__(self, uid, surface):	
        self.uid = uid
        w,h = surface.get_size()
        pygame.Rect.__init__(self, (0,0,w,h))
        
        self.tile_sz = 0 # tile size;
        self.cols = 0 # columns;
        self.rows = 0 # rows (true story);
        self.blank = None # blank tile holder;
        self.f_mob = None # f_mob = "following mob";
        self.scene = None
        
        print("camera initialized")

    def load_scene(self, fn, db, mob): # fn = "filename";
        if not(fn in db):
            db[fn] = scene.Scene(os.path.join(filepaths.scenes, fn), self) # advanced handling in Scene class?;
            print("loading scene:", fn)
        self.scene = db[fn]
        self.scene.camera = self
        self.f_mob = mob
        # assumes the tile is square
        self.cols = int(self.w / self.scene.tile_w + 2)
        self.rows = int(self.h / self.scene.tile_h + 2)
        self.blank = pygame.Surface((self.scene.tile_w,self.scene.tile_h)).convert()
        self.blank.fill((0,0,0))
        
        #self.controller.flush()
        #self.f_mob.moving = False TODO uncomment
        #self.sprites["player"].facing = "south" TODO put this somewhere else (like in a gamestate)
        self.update([], 0)
        
    def tile_prep(self, col, row): # (self, layer, col, row);
        x_off = self.x % self.scene.tile_w
        y_off = self.y % self.scene.tile_h
        c_idx = int(self.x / self.scene.tile_w + col) # column index
        r_idx = int(self.y / self.scene.tile_h + row) # row index
        return(col * self.scene.tile_w - x_off,
               row * self.scene.tile_h - y_off,
               c_idx, r_idx
              )

    def y_sort(self):
        return sorted(scene.live_mobs.values(),
                      key=operator.attrgetter('y')
                     )
            
    def update(self, signals, fc):
        if self.scene: self.scene.update(signals, fc)
        
        '''x,y = self.f_mob.center
        
        if x > self.w / 2:
            self.x = x - self.w / 2
        elif x <= self.w / 2:
            self.x = 0
        
        if y > self.h / 2:
            self.y = y - self.h / 2
        elif y <= self.h / 2:
            self.y = 0
    
        if self.x + self.w > self.scene.cols * self.tile_w:
            self.x = self.scene.cols * self.tile_w - self.w
        elif self.x < 0:
            self.x = 0
            
        if self.y + self.h > self.scene.rows * self.tile_h:
            self.y = self.scene.rows * self.tile_h - self.h
        elif self.y < 0:
            self.y = 0'''

    def render(self, surface):
        '''spr_draw = 0                
        for row in range(self.rows):
            for col in range(self.cols):
                for layer in ("bottom", "middle", "top"):    
                    x, y, c_idx, r_idx = self.tile_prep(col, row)
                    #if layer == "top":
                    #    if spr_draw == 0 and self.scene.live_mobs: # draw the sprites
                    #spr_draw = 1
                    for mob in self.y_sort():
                        mob.render(surface, x_off = -self.x, y_off = -self.y)
                    
                    tile_idx = self.scene.get_tile(layer, c_idx, r_idx)
                    if tile_idx == '0' and layer == 'bottom':
                        surface.blit(self.blank, (x,y))
                    if tile_idx != '0':
                        tile = self.scene.tileset[tile_idx]
                        surface.blit(tile, (x,y))'''

        for row in range(self.rows): # draw the bottom and middle tile layers
            for col in range(self.cols):
                x_offset = self.x % self.tilesize
                y_offset = self.y % self.tilesize

                c_index = int(self.x / self.tilesize + col)
                r_index = int(self.y / self.tilesize + row)
        
                bottom_i = self.scene.get_tile("bottom", c_index, r_index)
                middle_i = self.scene.get_tile("middle", c_index, r_index)

                c = col * self.tilesize - x_offset
                r = row * self.tilesize - y_offset
                
                if bottom_i != "0":
                    bottom_t = self.scene.tileset_obj[bottom_i]
                    self.game.display.blit(bottom_t, (c,r))
                elif bottom_i == "0":
                    self.game.display.blit(self.blank, (c,r))

                if middle_i != "0":
                    middle_t = self.scene.tileset_obj[middle_i]
                    self.game.display.blit(middle_t, (c,r))

        #if self.scene.loot: # TODO merge this with sprites for the y_sort
        #	for loot in self.scene.loot.values():
        #		loot.render(self.game.display, x_offset = -self.x, y_offset = -self.y)

        if self.game.scene_obj.live_mobs: # draw the sprites
            #for sprite in self.scene.sprites.values():
            for sprite in self.y_sort():
                sprite.render(self.game.display, x_off = -self.x, y_off = -self.y)
        
        for row in range(self.rows): # draw the top layer
            for col in range(self.cols):
                tile, x, y = self.tile_prep("top", col, row)
                if tile != "0": self.game.display.blit(tile, (x, y))
