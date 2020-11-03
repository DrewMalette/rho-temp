# __init__.py:

import glob

def import_mods():
    modules = glob.glob('*.py')
    for mod in modules:
        mn = mod.split('.')[0]  # mn = module name;
        if mn != '__init__':
            __import__(mn)
            
import_mods
