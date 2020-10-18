# utils.py:

import os
import xml.etree.ElementTree as ET

import pygame

from . import tileset
from . import filepaths

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
    cols = int(img.get_width() / w)
    rows = int(img.get_height() / h)
    for r in range(rows):
        for c in range(cols):
            x = c * w
            y = r * h
            tiles[str(gid)] = img.subsurface(x,y,w,h)
            gid += 1
    return tiles
    
def l_tmx(fn, scene_obj):
	tree = ET.parse(fn)
	root = tree.getroot()
	
	scene_obj.cols = int(root.attrib["width"])
	scene_obj.rows = int(root.attrib["height"])
	
	scene_obj.tile_w = int(root.attrib["tilewidth"])
	scene_obj.tile_h = int(root.attrib["tileheight"])
	#scene_obj.tilesize = scene_obj.tile_w # assumes a square tile
	
	scene_obj.tileset = tileset.Tileset(scene_obj.tile_w, scene_obj.tile_h)
	
	for tilesettag in root.iter("tileset"):
		filename = tilesettag.attrib["source"]
		tsxtree = ET.parse(os.path.join(filepaths.scenes, filename))
		tsxroot = tsxtree.getroot()
		for tsx in tsxroot.iter("tileset"):
			for i in tsx.iter("image"):
				fn = i.attrib["source"] # fn = 'filename';
				firstgid = tilesettag.attrib["firstgid"]
				scene_obj.tileset.add(fn, firstgid)
				
	for layer in root.iter("layer"):
		for data in layer.iter("data"):
			name = layer.attrib['name']
			rawdata = data.text.split(",")
			cleandata = []
			for tile in rawdata:
				cleandata.append(tile.strip())
			scene_obj.layers[name] = cleandata
			
	for layer in root.iter("objectgroup"):
		for rect in layer.iter("object"):
			rectattribs = {}
			for v in rect.attrib.keys():
				rectattribs[v] = rect.attrib[v]
			for proptag in rect.iter("properties"):
				for propchild in proptag.iter("property"):
					index = propchild.attrib["name"]
					value = propchild.attrib["value"]
					rectattribs[index] = value
			
			uid = rectattribs["id"]
			col = int(float(rectattribs["x"]) / scene_obj.tile_w)
			row = int(float(rectattribs["y"]) / scene_obj.tile_h)
			if rectattribs["type"] == "player":
				if scene_obj.game.player is None:
					print("player object is not defined")
					print("exiting")
					pygame.quit()
					exit()
				scene_obj.live_mobs["player"] = scene_obj.game.player
				scene_obj.live_mobs["player"].scene_obj = scene_obj
				scene_obj.live_mobs["player"].place(col, row)
			elif rectattribs["type"] == "switch":
				x = int(float(rectattribs["x"]) / scene_obj.tile_w) * scene_obj.tile_w
				y = int(float(rectattribs["y"]) / scene_obj.tile_h) * scene_obj.tile_h
				facing = rectattribs["facing"]
				try:
					c = int(rectattribs["col"])
					r = int(rectattribs["row"])
					scene_obj.switches[uid] = [pygame.Rect((x,y,scene_obj.tile_w,scene_obj.tile_h)), rectattribs["Filename"], (c,r), facing]
				except:
					#print("defaulting to map defined placement position")
					scene_obj.switches[uid] = [pygame.Rect((x,y,scene_obj.tile_w,scene_obj.tile_h)), rectattribs["Filename"], None, facing]
			elif rectattribs["type"] == "mob":
				scene_obj.add_mob(mob.Mob(filepaths.images + rectattribs["Filename"], rectattribs["name"]), col, row)
				#utils.place(scene_obj.live_mobs[uid], col, row, scene_obj)
			#elif rectattribs["type"] == "static":
			#	filepath = "content/image/" + rectattribs["Filename"]
			#	name = rectattribs["name"]
			#	scene.sprites[uid] = sprite.Static(filepath, name)
			#	scene.sprites[uid].scene = scene
			#	scene.sprites[uid].place(col,row)
