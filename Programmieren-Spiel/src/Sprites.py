class Sprite():
    def __init__(self,x,y,Sprite,Controller,BotState = None,):
        self.x = x
        self.Controller = Controller
        self.y = y
        self.Sprite = Sprite
        self.Spritetype = ""
        if Sprite == "Bot":
            if BotState == None:
                self.Controller.Logger.log("If you add a Bot please input the BotState")
            else:
                self.sprite = BotState
        else:
            self.sprite = Sprite
            self.Spritetype = "Item"
        self.Controller.Logger.log("Succesfully Initialized Sprite")
    def Change_BotState(self,BotState):
        if BotState == None:
            self.Controller.Logger.log("Please tell me your new Botstate")
        else:
            self.sprite = BotState
    def Change_Coords(self,Coords):
        if Coords == None:
            self.Controller.Logger.log("Please tell me the new Coordinates")
        else:
            self.x = Coords[0]
            self.y = Coords[1]