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
FLAGS = pygame.FULLSCREEN

# try not to obfuscate the code

class Game:
    def __init__(self):
        self.obj_stack = []                  # the most important list in the program;
        # proposal:
        # obj_stack = { 0:{}, 1:{}, 2:{} }
        self.signals = []                    # for objects to send signals to each other;
        self.fc = 0                          # frame counter;
        self.sprite_db = {}                  # spriteset database;
        self.tiles_db = {}                   # tileset database;
        # for the above 2, a utility function processes .png files;
        # the resulting data is stored in an instance of the appropriate class;
        self.scene_db = {}                   # Scene;
        self.sound_db = {}                   # .ogg files;
        # game objects;
        self.mob_db = {}                       # combines a Spritesheet with mechanics;
        self.ui = {}                         # user interface; dict or subsystem?;

        pygame.init()
        self.display = pygame.display.set_mode(SCR_SIZE)
        self.clock = pygame.time.Clock()
        self.camera = core.Camera("camera", display)
        self.fader = core.Fader("fader", display.get_size())
        self.p_input = core.Keyboard() # p_input = "player input";
    
        self.funcs = [] # functions

        self.running = False

        self.mode = "TitleScreen"

        self.modes = { "TitleScreen": [] }

        # gets the script entry point;
        #scr_main = importlib.import_module("scripts.main")
    
        # obj_stack = [ fader, camera, ui ]
        #camera.load_scene("apartment.tmx", db_scn, None) # player
        #obj_stack.append(camera)

        # define list stacks here; bind to dictionary
        # menu = [ Scene, ui["PlayerMenu"] ]
        # menu.append(thing)
        # ui["PlayerMenu"]: if menu[-1] == self...
        # gameplay = [ Scene ]
        # game_modes = { "menu": menu, "gameplay": gameplay }

        # this is where user scripts are imported;
        # import header;
        # header.setup();
        #scr_main.start() # fn;
    
# Scene.render(self): self.game.render(self)
# Camera: variable manipulation
# Renderer: actual drawing

# Scene.update(self):
#   self.game.camera.update()

    def main(self):
        self.running = True
        while running:
            self.clock.tick(60)
            self.fc = (fc + 1) % 4294967296 # highest 32-bit int;
        
            self.p_input.update()

            for sign in signals:
                self.funcs[sign]()
            # should this go before or after obj processes?
            #  before; a signal can modify obj_stack;

            for obj in self.modes[self.mode]:
                obj.update(self.signals, self.fc) # logic before graphics;
                obj.render(self.display)
        
            if "EXIT!!" in signals or p_input.exit == 1:
                self.running = False

            pygame.display.flip()
            self.signals.clear()
        
if __name__ == "__main__": main()
