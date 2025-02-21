
import plyer
import os 

def get_asset_path() -> str:
    app_path = plyer.storagepath.get_application_dir()
    
    return os.path.join(app_path, "assets")

def get_icons_path() -> str:
    return os.path.join(get_asset_path(),"icons")

def get_assets(path:str) -> str:
    return os.path.join(get_asset_path, path)

