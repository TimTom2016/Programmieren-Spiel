import src.Bot_main as Bot_main
import src.File_Reader as File_Reader
import src.Renderer as Renderer
import src.Sprites as Sprites
import src.Commands as Commands
import src.Command_helper as Command_Helper
import src.logger as logger
import time
import string
class Controller():
    def __init__(self):
        self.delay = 0.5
        self.Logger = logger.Logger()
        self.Command_Identifier = Commands.Commandidentifier(self)
        self.Command_helper = Command_Helper.Command_Helper(self)
        self.raster_reader = File_Reader.Raster(self)
        self.renderer = Renderer.Renderer(self.raster_reader.rows, self.raster_reader.cols,self)
        self.script = self.renderer.Ask_Question("Please Enter your Script(Format: Spriptname.txt): ")
        self.script_reader = File_Reader.Code(self.script, self)
        self.Bot_Sprite = Sprites.Sprite(self.raster_reader.find_sprite(spritename="Bot")[0], self.raster_reader.find_sprite(spritename="Bot")[1], Sprite="Bot", BotState=self.raster_reader.find_sprite(spritename="Bot")[2],Controller=self)
        self.Bot = Bot_main.Bot(Sprite=self.Bot_Sprite, coordinates=[self.Bot_Sprite.x, self.Bot_Sprite.y], Botstate=self.Bot_Sprite.sprite,Controller=self)
        self.Sprites = []
        self.Logger.log("Succesfully Imported all Modules")
    def startup(self):
        spritenames = list(string.ascii_uppercase)
        for i in spritenames:
            if self.raster_reader.find_sprite(spritename="Item",ItemName=i)[0] == "":
                pass
            else:
                Sprite = Sprites.Sprite(self.raster_reader.find_sprite(spritename="Item",ItemName=i)[0], self.raster_reader.find_sprite(spritename="Item",ItemName=i)[1],i,Controller=self)
                self.Sprites.append(Sprite)
        self.Sprites.append(self.Bot)
        self.renderer.renderraster(self.Sprites)
        self.Logger.log("Succesfully started the System")
        time.sleep(self.delay)
    def main(self):
        while True:
            try:
                self.script_reader.read_next_line()
                self.renderer.renderraster(self.Sprites)
                time.sleep(self.delay)
                self.Logger.log("Succesfully started the Executed Command and rendered it to the Screen")
            except:
                self.Logger.log("Closed Program")
                return
controller = Controller()
controller.startup()
controller.main()
print("I am Done with Everything!")