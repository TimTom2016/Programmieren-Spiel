Botstates = ["<","^",">","*","∨"]

class Bot():
    def __init__(self, coordinates, Botstate):
        self.x,self.y = coordinates
        self.Botstate = Botstate
        self.direction = "up"

    def move(self, iterations):
        for i in range(iterations):
            if self.direction == "up":
                self.Botstate = Botstates[1]
                self.x += 1
            if self.direction == "right":
                self.Botstate = Botstates[2]
                self.y += 1
            if self.direction == "left":
                self.Botstate = Botstates[0]
                self.y -= 1
            if self.direction == "down":
                self.Botstate = Botstates[4]
                self.x -= 1

    def rotate(self,direction,Sprite):
        if direction == "r":
            if self.direction == "up":
                self.direction = "right"
                self.Botstate = Botstates[2]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "right":
                self.direction = "down"
                self.Botstate = Botstates[4]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "left":
                self.direction = "up"
                self.Botstate = Botstates[1]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "down":
                self.direction = "left"
                self.Botstate = Botstates[0]
                Sprite.Change_BotState(self.Botstate)
        elif direction == "l":
            if self.direction == "up":
                self.direction = "left"
                self.Botstate = Botstates[0]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "left":
                self.direction = "down"
                self.Botstate = Botstates[4]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "down":
                self.direction = "right"
                self.Botstate = Botstates[2]
                Sprite.Change_BotState(self.Botstate)
            elif self.direction == "right":
                self.direction = "up"
                self.Botstate = Botstates[1]
                Sprite.Change_BotState(self.Botstate)

    def stop(self,Sprite):
        self.Botstate = Botstates[3]
        Sprite.Change_BotState(self.Botstate)