import configparser
import os

class CcSnake:
    LIB_PATH = os.path.abspath(__file__)
    LIB_DIR = os.path.dirname(LIB_PATH)
    LIB_NAME = os.path.basename(LIB_PATH)

    configEx = "txt"

    class Module:
        def RunModule(moduleName):
            try:
                with open(f"{CcSnake.LIB_DIR}/{moduleName}.ccsnake", "r+", encoding="utf-8") as module_file:
                    module_lines = module_file.readlines()
                    ex = "\n".join(module_lines)
                    try: exec(ex)
                    except Exception as e: return False, e

            except Exception as e:
                return False, e

        def PythonIsExist(module: any):
            try: __import__(str(module)); return True
            except ImportError: return False

    class Config:
        def SetFile(path: any):
            config.read(str(path))

config = configparser.ConfigParser()
config.read(f"{CcSnake.LIB_DIR}/{CcSnake.LIB_NAME}.{CcSnake.configEx}") # Default