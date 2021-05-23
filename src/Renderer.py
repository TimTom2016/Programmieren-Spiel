import platform
from os import system
class Renderer():
    def __init__(self,rows,cols):
        self.raster = []
        os = platform.system()
        if os == "Linux":
            self.cleancmd = "clear"
        if os == "Windows":
            self.cleancmd = "cls"
        self.rows = rows
        self.cols = cols
        self.standardrow = "#" + "."*(cols - 2) + "#"
        for i in range(rows):
            if i == 0:
                self.raster.append(())
            self.raster.append(self.standardrow)

    def clear(self):
        system(self.cleancmd)

    def renderraster(self,Sprite = []):
        if Sprite == []:
            print("Please add a Sprite list")
        else:
            for i in range(Sprite):
                return 
