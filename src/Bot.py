# class where all possible botStates are defined
class botStates:
    def __init__(self):
        self.arrows = ["^", ">", "v", "<"]
        self.states = ["N", "E", "S", "W"]
        self.stopArrow = "o"
        self.stopState = "o"
        self.isStopped = False
        self.state = ""
    
    # stopping the bot
    def toggleStop(self):
        self.isStopped = not self.isStopped
    
    # setting the state of the bot
    def set(self, state):
        if state in self.arrows:
            self.state = self.convertToState(state)
        elif state in self.states:
            self.state = state
    
    # setting next state
    def setNext(self):
        if self.isStopped:
            self.state = self.stopState
        else:
            self.state = self.states[(self.states.index(self.state) + 1) % len(self.states)]
    
    # setting last state
    def setPrevious(self):
        if self.isStopped:
            self.state = self.stopState
        else:
            self.state = self.states[(self.states.index(self.state) - 1) % len(self.states)]
    
    # converting state to arrow
    def convertToArrow(self,state):
        if self.isStopped:
            return self.stopArrow
        for i in range(len(self.states)):
            if state == self.states[i]:
                return self.arrows[i]

    # converting arrow to state    
    def convertToState(self, arrow):
        if self.isStopped:
            return self.stopState
        for i in range(len(self.arrows)):
            if arrow == self.arrows[i]:
                return self.states[i]
    
    # getting stop state
    def getStopState(self):
        return self.stopState
    
    # getting the state
    def get(self):
        return self.state
    


class Bot:
    def __init__(self, Controller):
        self.Controller = Controller
        self.x,self.y = 0,0
        self.botState = botStates()
        self.LastState = ""
        self.stopped = False
    
    # second init function because we can't be sure that Raster is initialized when the first init function is called
    def init(self):
        if self.Controller.Raster.initialized == False:
            self.Controller.Raster.init()
            self.Controller.Logger.log("WARNING","Raster initialized because it was not initialized before")
        self.x,self.y = self.Controller.Raster.getBotCoordinates()
        self.botState.set(self.Controller.Raster.getBotState())
        self.Controller.Raster.replace(self.x, self.y, self.getIcon())
        self.Controller.Logger.log("INFO","Bot initialized")
    
    # moving the bot
    def move(self, count=1):
        if self.stopped:
            self.Controller.Logger.log("DEBUG","Bot is stopped")
            return
        if count < 1:
            self.Controller.Logger.log("WARNING","Count is smaller than 1")
            return
        direction = self.botState.get()
        if direction == "N":
            self.y -= count
        elif direction == "E":
            self.x += count
        elif direction == "S":
            self.y += count
        elif direction == "W":
            self.x -= count
        self.update()

    # rotating the bot
    def rotate(self,direction):
        if self.stopped:
            self.Controller.Logger.log("DEBUG","Bot is stopped")
            return
        self.LastState = self.botState.get()
        if direction != "L" or direction != "R":
            if direction == "N":
                self.botState.set("N")
            elif direction == "E":
                self.botState.set("E")
            elif direction == "S":
                self.botState.set("S")
            elif direction == "W":
                self.botState.set("W")
        else:    
            if direction == "L":
                self.botState.setPrevious()
            elif direction == "R":
                self.botState.setNext()
        self.update()

    # getting the direction of the bot
    def getDirection(self):
        return self.botState.get()

    # getting the icon of the bot
    def getIcon(self):
        return self.botState.convertToArrow(self.botState.get())
    
    # getting the coordinates of the bot
    def getCoordinates(self):
        return [self.x,self.y]

    # stopping the bot
    def toggleStop(self):
        self.stopped = not self.stopped
        self.botState.toggleStop()
        if not self.stopped:
            if self.LastState != "":
                self.botState.set(self.LastState)
            else:
                self.botState.set("N")
        self.update()
    
    # updating the bot
    def update(self):
        beforeX, beforeY = self.Controller.Raster.getBotCoordinates()
        self.Controller.Raster.move(beforeX,beforeY, self.x, self.y)
        self.Controller.Raster.replace(self.x, self.y, self.getIcon())
        self.Controller.Logger.log("DEBUG","Bot updated")