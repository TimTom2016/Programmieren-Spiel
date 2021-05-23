from Bot_main import Botstates
class Raster():
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.raster = []
        with open("raster.txt","r") as f:
            for i in f:
                if i.startswith("#"):
                    self.rows += 1
                    self.raster.append(i)
            for i in range(len(self.raster[0])):
                self.cols += 1
    def find_sprite(self,spritename,ItemName = None):
        x = 0
        y = 0
        if spritename == "Bot":
            for i in Botstates:
                for r in self.raster:
                    if x.find(i) != None:
                        y = x.find(i)
                        return x, y
                    x += 1
        if spritename == "Item":
            if ItemName == None:
                print("Please enter Name of Item like \"C\"")
            else:
                for r in self.raster:
                    if x.find(ItemName) != None:
                        y = x.find(i)
                        return x, y
                    x += 1