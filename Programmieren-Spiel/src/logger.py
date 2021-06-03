from datetime import datetime
class Logger():
    def __init__(self):
        self.time = datetime.now().strftime("%H:%M:%S")
        self.time = self.time.replace(":","-")
        with open("src/logs/"+str(self.time)+"-log.txt", "a") as f:
            pass
    def log(self,text):
        with open("src/logs/"+str(self.time)+"-log.txt","a") as f:
            f.write(datetime.now().strftime("%H:%M:%S")+": "+text+"\n")