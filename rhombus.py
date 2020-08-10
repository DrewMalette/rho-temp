# rhombus.py:
import sys, importlib
import pygame

from . import core
from . import mech

# sets the screen size;
SCR_SIZE = (640,480)
# appends the root path to namespace;
sys.path.append("./")
# gets the script entry point;
scr_main = importlib.import_module("scripts.main")
# the most important list in the program;
obj_stack = []
# for objects to send signals to each other;
signs = []
# frame counter;
fc = 0
# resource database;
self.db_spr = {} # Spriteset;
self.db_tls = {} # Tileset;
# for the above 2, a utility function processes .png files;
# the resulting data is stored in an instance of the appropriate class;
self.db_scn = {} # Scene;
self.db_snd = {} # .ogg files;
# game objects;
self.mobs = {} # combines a Spritesheet with mechanics;
self.ui = {} # dict or subsystem?;
# the low-level implementation is in utilities;
def l_spr(fn): # load spriteset;
    if fn not in db_spr:
        db_spr[fn] = core.Spriteset(fn)

def l_tls(fn): # load tileset;
    if fn not in db_tls:
        db_tls[fn] = core.Tileset(fn)

def main():
    pygame.init()
    display = pygame.display.set_mode(SCR_SIZE)
    clock = pygame.time.clock()
    camera = core.Camera("camera", (0,0), display.get_size())

    # this is where user scripts are imported;
    # import header;
    # header.setup();
    scr_main.start() # fn;

    running = True
    while running:
        clock.tick(60)
        fc = (fc + 1) % 4294967296 # highest 32-bit int;

        for obj in obj_stack:
            obj.update(signs, fc) # logic before graphics;
            obj.render(display)

        if "EXIT!!" in signs:
            running = False

        signals.clear()
