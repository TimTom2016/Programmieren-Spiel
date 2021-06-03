from src.Bot_main import Botstates
import os
class Raster():
    def __init__(self,Controller):
        self.Controller = Controller
        self.rows = 0
        self.cols = 0
        self.Grid = []
        with open("src/Levels/Grid.txt", "r") as f:
            for i in f:
                if i.startswith("#"):
                    self.rows += 1
                    self.Grid.append(i)
            for i in range(len(self.Grid[0])):
                self.cols += 1
            self.cols -= 1
        self.Controller.Logger.log("Succesfully created Raster from Grid.txt")
        self.Controller.Logger.log("Succesfully Initialized Raster_Reader")
    def find_sprite(self,spritename,ItemName = None):
        x = 0
        y = 0
        direction = ""
        if spritename == "Bot":
            for i in Botstates:
                for r in self.Grid:
                    if r.find(i) >= 0:
                        y = r.find(i)
                        self.Controller.Logger.log("Succesfully found Bot in Raster at " + str((x+1)) + str(y))
                        return (x+1), y , i
                    x += 1
                x = 0
                y = 0
            direction += 1
        if spritename == "Item":
            if ItemName is None:
                self.Controller.Logger.log("Please enter Name of Item like \"C\"")
            else:
                for r in self.Grid:
                    if r.find(ItemName) >= 1:
                        y = r.find(ItemName)
                        self.Controller.Logger.log("Succesfully found " + ItemName + " in Raster at "+str(x)+str(y))
                        return x, y
                    x += 1
                self.Controller.Logger.log("Succesfully could't find " + ItemName + " in Raster")
                return "" , ""

    def look(self,coords = []):
        if coords == []:
            self.Controller.Logger.log("Coordinates are not complete")
        else:
            self.Controller.Logger.log("Found "+self.Grid[coords[0]][coords[1]]+" at x: "+ coords[0]+" y: "+coords[1])
            return self.Grid[coords[0]][coords[1]]
class Code():
    def __init__(self,scriptname,Controller):
        self.lines = []
        self.Controller = Controller
        self.current_line = 0
        self.Command_Helper = self.Controller.Command_helper
        self.Commandidentifier = self.Controller.Command_Identifier
        with open("src/scripts/"+scriptname,'r') as f:
            for i in f:
                if i.startswith('#'):
                    pass
                elif i.startswith('\n'):
                    pass
                else:
                    self.lines.append(i[:-1])
        self.Controller.Logger.log("Script is "+str(self.lines))
        self.Controller.Logger.log("Succesfully Initialized Code_Reader")
    def read_next_line(self):
        self.Commandidentifier.identify(cmd=self.lines[self.current_line])
        self.current_line += 1
class Config():
    def __init__(self,scriptname):
        self.lines = []
        with open("Config/"+scriptname,'r') as f:
            for i in f:
                if i.startswith('#'):
                    pass
                if i.startswith('\n'):
                    pass
            self.lines.append(i[:-1])
class Language():
    def __init__(self):
        self.Languages = []
        self.Languages_Files = os.listdir('Language')
        lines = []
        for i in self.Languages_Files:
            with open("Language/" + i, 'r') as f:
                for i in f:
                    if i.startswith('#'):
                        pass
                    if i.startswith('\n'):
                        pass
                lines.append(i[:-1])
            self.Languages.append([i[:-4],lines])