import platform
import os as OS
class Renderer():
    def __init__(self,Controller):
        self.controller = Controller
        self.initiated = False
        self.text = {}
        self.cleanCmd = self.detectClearCmd()
        self.controller.Logger.log("INFO","Succesfully created Renderer")
    
    # setting the clean command
    def detectClearCmd(self):
        os = platform.system()
        if os == "Linux":
            return "clear"
        elif os == "Windows":
            return "cls"
        
    # second init function because the first one is called before the raster is created
    def init(self):
        self.initiated = True
        if self.controller.raster.initialized == False:
            self.controller.Logger.log("ERROR","Raster not initialized before the renderer, automatically initializing")
            self.controller.Raster.init()
        self.getRaster()
        self.controller.Logger.log("INFO","Succesfully initialized Renderer")

    # function used to get the raster from the controller
    def getRaster(self):
        self.raster = self.controller.Raster
    
    # Clears the console
    def clear(self):
        OS.system(self.cleanCmd)

    # Renders the raster and the text
    def renderRaster(self):
        self.clear()
        raster = []
        for line in self.raster.getGrid():
            raster.append([Icon.getIcon() for Icon in line])
        for line in raster:
            print(line+"\n")
        for key in self.text:
            print(self.text[key])
        self.controller.Logger.log("DEBUG","Successfully rendered the raster")
    
    # adding text to the renderer
    def addText(self,key,text):
        self.text[key] = text
    
    # removing text from the renderer
    def removeText(self,key):
        del self.text[key]