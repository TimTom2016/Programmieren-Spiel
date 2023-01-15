from unittest import skip
import rasterItems
import os
class Raster():
    def __init__(self,Controller,grid):
        self.initiated = False
        self.Controller = Controller
        self.gridFile = grid
        self.Grid = []
        
    # Second init function, to make everything compatible with the new other classes
    def init(self):
        self.initiated = True
        self.createGridFromTxt(self.gridFile)
        self.Controller.Logger.log("INFO","Successfully created a grid from an txt file")
    

    # Creates a grid from a txt file
    def createGridFromTxt(self,grid):
        self.Grid = []
        with open("Levels\\"+grid+".txt","r") as file:
            for line in file:
                line = line.replace("\n","")
                if line.startswith("//"):
                    pass
                else:
                    for symbol in line:
                        lineObjects = []
                        x = line.index(symbol)
                        y = self.Grid.index(line)
                        lineObjects.append(rasterItems.createRightObject(symbol,x,y))
                    self.Grid.append(lineObjects)

    # resets the grid to the original state
    def reset(self):
        self.createGridFromTxt(self.gridFile)
        self.Controller.Logger.log("DEBUG","Successfully reset the grid")

    # searches for a specific item in the grid and returns the coordinates of the first occurrence
    def search(self,searchFor):
        for line in self.Grid:
            for item in line:
                if item.getIcon() == searchFor:
                    return item.getCoordinates()
    
    # searches for a specific item in the grid and returns the coordinates of all occurrences
    def searchAll(self,searchFor):
        coordinates = []
        for line in self.Grid:
            for item in line:
                if item.getIcon() == searchFor:
                    coordinates.append(item.getCoordinates())
        return coordinates

    # gets the Icon at a specific coordinate
    def look(self,x,y):
        return self.Grid[y][x].getIcon()
    
    # replaces an item in the grid with a new item
    def replace(self,x,y,newItem):
        del self.Grid[y][x]
        self.Grid[y][x] = rasterItems.createRightObject(newItem,x,y)
    
    # clears a specific cell
    def clearCell(self,x,y):
        self.replace(x,y,".")

    # Simple macro to move an item from x,y to x2,y2
    def move(self,beforeX,beforeY,afterX,afterY):
        self.replace(afterX,afterY,self.look(beforeX,beforeY))
        self.clearCell(beforeX,beforeY)
    
    # returns the grid
    def getGrid(self):
        return self.Grid
    
    # returns the size of the grid
    def getSize(self):
        return [len(self.Grid[0]),len(self.Grid)]

    # updates the bot state
    def updateBot(self,bot):
        self.replace(bot.x,bot.y,bot.getIcon())

    # gets the bot and returns the coordinates of the cell he is on
    def getBotCoordinates(self):
        for line in self.Grid:
            for item in line:
                if item.__class__.__name__ == "Bot":
                    return item.getCoordinates()
    
    # gets the bot and returns the state he is in
    def getBotState(self):
        for line in self.Grid:
            for item in line:
                if item.__class__.__name__ == "Bot":
                    return item.getIcon()
    

        

class Code():
    def __init__(self,scriptname,Controller):
        self.lines = []
        self.Controller = Controller
        self.whileline = 0
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