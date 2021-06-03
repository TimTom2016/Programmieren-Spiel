import platform
import os as OS
import time
class Renderer():
    def __init__(self,rows,cols,Controller):
        self.raster = []
        self.Controller = Controller
        os = platform.system()
        if os == "Linux":
            self.cleancmd = "clear"
        if os == "Windows":
            self.cleancmd = "cls"
        self.rows = rows
        self.cols = cols
        self.standardrow = "#" + "."*(self.cols - 2) + "#"
        for i in range(rows):
            if i == 0:
                self.raster.append(("#"*self.cols))
            else:
                self.raster.append(self.standardrow)
        self.raster.append(("#" * self.cols))
        self.Controller.Logger.log("Created Render Raster")
        self.Controller.Logger.log("Succesfully Initialized Renderer")
    def clear(self):
        OS.system(self.cleancmd)

    def renderraster(self,Sprites):
        OS.system(self.cleancmd)
        raster = []
        for y in self.raster:
            raster.append(y)
        if not Sprites:
            print("Please add a Sprite list")
        else:
            for i in Sprites:
                raster[i.x] = str(raster[i.x][:i.y]) + str(i.sprite) + str(raster[i.x][i.y + 1:])
            for x in raster:
                print(x)

    def Ask_Question(self,Question,Possible_Answers = None):
        OS.system(self.cleancmd)
        print(Question)
        answer = input("Answer? ")
        if Possible_Answers == None:
            self.Controller.Logger.log("Asked " + Question + " and got " + answer + " as answer ")
            return answer
        if Possible_Answers == "Sprites":
            self.Controller.Logger.log("Asked for Sprites and got "+answer+" as Answer: ")
            return answer
        for i in Possible_Answers:
            if answer.lower() == i.lower():
                self.Controller.Logger.log("Asked "+Question+" and got "+answer+" as answer ")
                return answer.lower()
    def RenderText(self,text):
        OS.system(self.cleancmd)
        print(text)
        time.sleep(self.Controller.delay)