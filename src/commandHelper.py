commands = {}
def registerCommand(self,command):
    commands[command.__name__] = command
class CommandHelper:
    def __init__(self,controller):
        self.controller = controller
        self.controller.Logger.log("INFO","Succesfully created CommandHelper")
    def move(self,iterations):
        """
        Moves the bot, you can use iterations to move the bot multiple times
        @param iterations: The amount of times you want to move the bot, 0 and below will throw an error
        """
        self.controller.Logger.log("DEBUG","Moving "+dir)
        self.controller.Bot.move(iterations)
    def rotate(self,dir):
        """
        Rotates the bot, you can use the following directions: L,R
        @param dir: The direction you want to rotate the bot to
        """
        self.controller.Logger.log("DEBUG","Rotating "+dir)
        self.controller.Bot.rotate(dir)
    def setDir(self,dir):
        """
        Sets the direction of the bot, you can use the following directions: N,E,S,W
        @param dir: The direction you want to set the bot to
        """
        self.controller.Logger.log("DEBUG","Setting direction to "+dir)
        self.controller.Bot.botstate(dir)
    def toggleStop(self):
        """
        Toggles the stop state of the bot
        """
        self.controller.Logger.log("DEBUG","Stopping bot")
        self.controller.Bot.toggleStop()
