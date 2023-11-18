from collections import UserDict
import json
import os

class Settings(UserDict):
    def __getattr__(self, name):
        return self.__getitem__(name.upper())

    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __setitem__(self, name, value):
        name = name.upper()
        super().__setitem__(name, Settings(value) if isinstance(value, dict) else value)
    
    def load(self, pathlist: list | str):
        for path in [pathlist] if isinstance(pathlist, str) else pathlist:
            if os.path.exists(path):
                with open(path) as f:
                    self.update(json.load(f))
