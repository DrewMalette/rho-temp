# tileset.py:

import os

import pygame

#from . import fpaths # filepaths
from . import utils

class Tileset:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.tiles = {}

    def add(self, fn, firstgid=1):
        tiles = utils.l_img_tls(os.path.join(fpaths.scn_path, fn, self.w, self.h, firstgid))
        self.tiles.update(tiles)

    def __getitem__(self, key=-1):
        if key == -1:
            return self.tiles
        else:
            return self.tiles[key]
