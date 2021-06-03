Botstates = ["<","^",">","*","∨"]

class Bot():
    def __init__(self, coordinates, Botstate,Sprite,Controller):
        self.Controller = Controller
        self.x,self.y = coordinates
        self.Botstate = Botstate
        if Botstate == Botstates[0]:
            self.direction = "left"
        if Botstate == Botstates[1]:
            self.direction = "up"
        if Botstate == Botstates[2]:
            self.direction = "right"
        if Botstate == Botstates[3]:
            self.direction = "stop"
        if Botstate == Botstates[4]:
            self.direction = "down"
        self.Sprite = Sprite
        self.sprite = self.Botstate
        self.Spritetype = "Bot"
        self.Controller.Logger.log("Succesfully Created Bot")

    def move(self, iterations):
        for i in range(iterations):
            if self.direction == "up":
                if 1 == self.x:
                    self.Controller.Logger.log("Error You're moving out of the Gamefield")
                else:
                    self.x -= 1
            if self.direction == "right":
                if (self.Controller.raster_reader.cols - 2) == self.y:
                    self.Controller.Logger.log("Error You're moving out of the Gamefield")
                else:
                    self.y += 1
            if self.direction == "left":
                if 1 == self.y:
                    self.Controller.Logger.log("Error You're moving out of the Gamefield")
                else:
                    self.y -= 1
            if self.direction == "down":
                if (self.Controller.raster_reader.rows - 1) == self.x:
                    self.Controller.Logger.log("Error You're moving out of the Gamefield")
                else:
                    self.x += 1
        self.Sprite.Change_Coords([self.x, self.y])
        self.sprite = self.Botstate

    def rotate(self,direction):
        if direction == "r":
            if self.direction == "up":
                self.direction = "right"
                self.Botstate = Botstates[2]
            elif self.direction == "right":
                self.direction = "down"
                self.Botstate = Botstates[4]
            elif self.direction == "left":
                self.direction = "up"
                self.Botstate = Botstates[1]
            elif self.direction == "down":
                self.direction = "left"
                self.Botstate = Botstates[0]
            elif self.direction == "stop":
                self.direction = "right"
                self.Botstate = Botstates[2]
            self.Sprite.Change_Coords([self.x, self.y])
        elif direction == "l":
            if self.direction == "up":
                self.direction = "left"
                self.Botstate = Botstates[0]
            elif self.direction == "left":
                self.direction = "down"
                self.Botstate = Botstates[4]
            elif self.direction == "down":
                self.direction = "right"
                self.Botstate = Botstates[2]
            elif self.direction == "right":
                self.direction = "up"
                self.Botstate = Botstates[1]
            elif self.direction == "stop":
                self.direction = "left"
                self.Botstate = Botstates[0]
            self.Sprite.Change_Coords([self.x, self.y])
        self.sprite = self.Botstate
        self.Sprite.Change_Coords([self.x,self.y])
    def stop(self):
        self.Botstate = Botstates[3]
        self.sprite = self.Botstate
        self.direction = "stop"
        self.Sprite.Change_BotState(self.Botstate)