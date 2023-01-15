from datetime import datetime

# class used for everything that has to do with logging
class Logger():
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M:%S")
        self.time = self.time.replace(":","-")
        with open("src/logs/"+str(self.time)+"-log.txt", "a") as f:
            pass
        self.loggingLevels = ["INFO","WARNING","ERROR","DEBUG"]
        self.DeactivatedLevels = []
        self.log("INFO","Successfully created Logger")
    
    # logging text with different levels
    def log(self,type,text):
        with open("src/logs/"+str(self.time)+"-log.txt","a") as f:
            if type in self.loggingLevels:
                if type not in self.DeactivatedLevels:
                    f.write(self.getTime()+" : ["+type+"] "+text+"\n")
            else:
                f.write(self.getTime()+" : [INFO] "+text+"\n")
    

    # deactivating logging levels
    def deactivateLevel(self,level):
        if level in self.loggingLevels:
            self.DeactivatedLevels.append(level)
        else:
            self.log("WARNING","Tried to deactivate a non existing logging level")

    def activateLevel(self,level):
        if level in self.DeactivatedLevels:
            self.DeactivatedLevels.remove(level)
        else:
            self.log("WARNING","Tried to activate a non deactivated logging level")

    # getting the current time
    def getTime(self):
        return datetime.now().strftime("%H:%M:%S")