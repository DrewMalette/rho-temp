# camera.py:

import pygame

from . import scene

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

    def load_scene(self, fn, mob): # fn = "filename";
        self.scene = scene.Scene(fn, self) # advanced handling in Scene class?;
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
    
        #index = self.scene.get_tile(layer, c_idx, r_idx)

        return(c_idx, r_idx,
               col * self.scene.tile_w - x_off,
               row * self.scene.tile_h - y_off
              )
        
        #if index != "0":
        #    tile = self.scene.tileset[index]
        #    return (tile, x, y)
        #else:			
        #    return ("0", x, y)
    
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
    
        if self.x + self.w > self.scene.cols * self.tile_sz:
            self.x = self.scene.cols * self.tile_sz - self.w
        elif self.x < 0:
            self.x = 0
            
        if self.y + self.h > self.scene.rows * self.tile_sz:
            self.y = self.scene.rows * self.tile_sz - self.h
        elif self.y < 0:
            self.y = 0'''

    def render(self, surface):
        for row in range(self.rows): # draw the bottom and middle tile layers
            for col in range(self.cols):
                #x_off = self.x % self.tile_sz
                #y_off = self.y % self.tile_sz

                #c_idx = int(self.x / self.tile_sz + col)
                #r_idx = int(self.y / self.tile_sz + row)
                spr_draw = 0
                for layer in ("bottom", "middle", "top"):	
    
                    x, y, c_idx, r_idx = self.tile_prep(col, row)
                    if layer == "top":
                        if spr_draw == 0 and self.scene.live_mobs: # draw the sprites
                            spr_draw = 1
                            for mob in self.y_sort():
                                mob.render(surface,
                                           x_off = -self.x,
                                           y_off = -self.y
                                          )
                    
                    tile_idx = self.scene.get_tile(layer, c_idx, r_idx)
                    if tile_idx != '0':
                        tile = self.scene.tileset[tile_idx]
                        surface.blit(tile, (x,y))
                    
                    #bot_tile = self.scene.get_tile("bottom", c_idx, r_idx)
                    #mid_tile = self.scene.get_tile("middle", c_idx, r_idx)
                    #top_tile = self.scene.get_tile("top", c_idx, r_idx)

                #c = col * self.tile_sz - x_off
                #r = row * self.tile_sz - y_off
                
                #if bot_idx != "0":
                #    tile = self.scene.tileset[bot_idx]
                #    surface.blit(tile, (c,r))
                #elif bot_idx == "0" and :
                #    surface.blit(self.blank, (c,r))

                #if mid_idx != "0":
                #    tile = self.scene.tileset[mid_idx]
                #    surface.blit(tile, (c,r))

        #if self.scene.loot: # TODO merge this with sprites for the y_sort
        #	for loot in self.scene.loot.values():
        #		loot.render(surface, x_off = -self.x, y_off = -self.y)

        #if self.scene.live_mobs: # draw the sprites
            #for sprite in self.scene.sprites.values():
        #    for mob in self.y_sort():
        #        mob.render(surface, x_off = -self.x, y_off = -self.y)
        
        #for row in range(self.rows): # draw the top layer
        #    for col in range(self.cols):
        #        tile, x, y = self.tile_prep("top", col, row)
        #        if tile != "0": surface.blit(tile, (x, y))
        
        #if debug_info_on == 1:
        #    r = (player.action.x - self.x, player.action.y - self.y, player.action.w, player.action.h)
        #    pygame.draw.rect(surface, (0xff,0,0), r, 1)
