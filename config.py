import json
from importlib import resources

def cfg_item(*items):
    data = Config.instance().data
    for k in items:
        data = data[k]
    return data

class Config:

    __config_pack = "healthy.assets.config"
    __config_file = "config.json"
    __background_pack = "healthy.assets.config"
    __background_file = "config.json"
    __rect_pack = "healthy.assets.config"
    __rect_file = "config.json"
    __instance = None

    @staticmethod
    def instance():
        if Config.__instance is None:
            Config()
        return Config.__instance

    def __init__(self):
        if Config.__instance is None:
            Config.__instance = self
        else:
            raise Exception("Config can only be instanciated once!!!")

        with resources.path(Config.__background_pack, Config.__background_file) as background_path:
            with open(background_path) as b:
                self.data = json.load(b) 
                
        with resources.path(Config.__config_pack, Config.__config_file) as config_path:
            with open(config_path) as f:
                self.data = json.load(f)

        with resources.path(Config.__rect_pack, Config.__rect_file) as rect_path:
            with open(rect_path) as r:
                self.data = json.load(r)         
                #print (self.data)       

             

           



