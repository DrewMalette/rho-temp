# utils.py:

import pygame

# load image;
def l_img(fn, ckey=None): # colour key;
    try:
        img = pygame.image.load(fn)
    except:
        print("failed to load image '{}' ".format(fn))
        return
    img = img.convert()
    if ckey != None:
        if ckey == -1:
            ckey = img.get_at((0,0))
        img.set_colorkey(ckey, pygame.RLEACCEL)
    return img

# load image tilesheet;
def l_img_tls(fn, w, h, firstgid=1):
    img = l_img(fn, (255,0,255))
    gid = int(firstgid)
    tiles = {}
    cols = int(image.get_width() / w)
    rows = int(image.get_height() / h)
    for r in range(rows):
        for c in range(cols):
            x = c * w
            y = r * h
            tiles[str(gid)] = img.subsurface(x,y,w,h)
            git += 1
    return tiles
