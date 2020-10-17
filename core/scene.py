# scene.py:

class Scene:
    def __init__(self, fn): # fn = "filename"
        self.uid = fn
        
        self.mobs = {}
        self.live_mobs = {}
        #self.buildings = {}
        #self.furniture = {}
        #self.loot = {}
        #self.loot_count = 0
        self.switches = {}
        self.layerdata = { "bottom": None, "middle": None, "top": None, "collide": None }
        self.tileset = None
        
        utilities.load_tmx(self.filename, self)
        
        self.camera = None
        self.paused = False # ?;
        
    #def add_loot(self, fn, x, y):    
    #    uid = self.loot_count
    #    px = x
    #    py = y - 20
        #self.loot[self.loot_count] = sprite.Loot(self, uid, fn, (px,py))
        #self.loot_count = (self.loot_count + 1) % 256
        
    def add_mob(self, mob_obj):    
        self.mobs[mob.name] = mob_obj
    
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
