class Command_Helper():
    def __init__(self,Main_Controller):
        self.Controller = Main_Controller
        self.Controller.Logger.log("Succesfully initialized Command_Helper")
    def rotate(self,direction):
        self.Controller.Bot.rotate(direction)
        self.Controller.Logger.log("Rotated the bot to "+direction)
    def move(self,iterations):
        if str(iterations).isalnum() == True:
            iterations = int(iterations)
            self.Controller.Bot.move(iterations)
            self.Controller.Logger.log("Moved the Bot")
    def stop(self):
        self.Controller.Bot.stop()
        self.Controller.Logger.log("Stopped the Bot")
    def Print(self,arg):
        self.Controller.renderer.RenderText(arg)
        self.Controller.Logger.log("Wrote "+arg+" into the console")