
from utils.path_manager import get_icons_path
import os 

def get_icons():
    
    icons = []
    for root, dir, files in os.walk(get_icons_path()):
        for ic in files:
            icons.append(os.path.join(get_icons_path(), ic))
             
    return icons
