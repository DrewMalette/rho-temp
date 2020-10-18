# scene.py:

import utils

class Scene:
    def __init__(self, fn, grp=None): # fn = "filename"
        self.uid = fn
        self.camera = None
        self.paused = False # ?;
        self.mobs = {}
        self.live_mobs = {}
        #self.buildings = {}
        #self.furniture = {}
        #self.loot = {}
        #self.loot_count = 0
        self.switches = {}
        self.layers = { "bottom": None, "middle": None, "top": None, "collide": None }
        self.cols = int(root.attrib["width"])
	    self.rows = int(root.attrib["height"])
	    self.tile_w = int(root.attrib["tilewidth"])
	    self.tile_h = int(root.attrib["tileheight"])
        self.tileset = None
        utils.l_tmx(fn, self)
        if grp and type(grp).__name__ == 'list':
            self.grp = grp
            grp[self.uid] = self
        
    #def add_loot(self, fn, x, y):    
    #    uid = self.loot_count
    #    px = x
    #    py = y - 20
        #self.loot[self.loot_count] = sprite.Loot(self, uid, fn, (px,py))
        #self.loot_count = (self.loot_count + 1) % 256
        
    def add_mob(self, mob_obj, col, row):
        mob_obj.scene = self
        mob_obj.spawn_c = col
        mob_obj.spawn_r = row
        self.mobs[mob_obj.uid] = mob_obj
        mob_obj.spawn()
    
    def get_tile(self, layer, col, row):    
        index = int((row % self.rows) * self.cols + (col % self.cols))
        return self.layerdata[layer][index]
            
    def update(self, signals, fc):        
        #if not self.game.fader.fading and not self.paused:
        if not "fading" in signals and not self.paused:
            for mob in self.live_mobs.values():
                mob.update()
    
    # not needed?;    
    #def render(self, surface):    
    #    self.camera.render(surface)
