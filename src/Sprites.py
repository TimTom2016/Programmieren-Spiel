class Sprite():
    def __init__(self,x,y,Sprite,BotState = None):
        self.x = x
        self.y = y
        if Sprite == "Bot":
            if BotState == None:
                print("If you add a Bot please input the BotState")
            else:
                self.sprite = BotState
    def Change_BotState(self,BotState):
        if BotState == None:
            print("Please tell me your new Botstate")
        else:
            self.sprite = BotState
    def Change_Coords(self,Coords):
        if Coords == None:
            print("Please tell me the new Coordinates")
        else:
            self.x = Coords[0]
            self.y = Coords[1]