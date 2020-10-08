# just needed a wee break; this is rhombus: reloaded, folks;
# October 4, 2020: project resumed;
#
# can I somehow thread a prompt to insert signals into the 'signals' dict?;
#
# rhombus.py:
import sys, importlib
import pygame

sys.path.append("./")       # appends the root path to namespace;

import core
#from . import mech

SCR_SIZE = (640,480)        # sets the screen size;

# the low-level implementation is in utilities;
def l_spr(fn): # load spriteset; fn = filename;
    if fn not in db_spr:
        db_spr[fn] = core.Spriteset(fn)

def l_tls(fn): # load tileset;
    if fn not in db_til:
        db_til[fn] = core.Tileset(fn)

def main():
    obj_stack = []                  # the most important list in the program;
    signals = []                    # for objects to send signals to each other;
    fc = 0                          # frame counter;
    db_spr = {}                     # spriteset database;
    db_til = {}                     # tileset database;
    # for the above 2, a utility function processes .png files;
    # the resulting data is stored in an instance of the appropriate class;
    db_scn = {}                     # Scene;
    db_snd = {}                     # .ogg files;
    # game objects;
    mobs = {}                       # combines a Spritesheet with mechanics;
    ui = {}                         # dict or subsystem?;

    pygame.init()
    display = pygame.display.set_mode(SCR_SIZE)
    clock = pygame.time.Clock()
    #camera = core.Camera("camera", (0,0), display.get_size())
    controller = core.Controller()

    # gets the script entry point;
    #scr_main = importlib.import_module("scripts.main")

    # this is where user scripts are imported;
    # import header;
    # header.setup();
    #scr_main.start() # fn;

    running = True
    while running:
        clock.tick(60)
        fc = (fc + 1) % 4294967296 # highest 32-bit int;

        for sign in signals:
            funcs[sign]()
        # should this go before or after obj processes?
        #  before; a signal can modify obj_stack;

        for obj in obj_stack:
            obj.update(signals, fc) # logic before graphics;
            obj.render(display)

        if "EXIT!!" in signals:
            running = False

        signals.clear()
        
if __name__ == "__main__": main()
