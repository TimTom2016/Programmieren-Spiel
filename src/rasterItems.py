class Objects:
    def __init__(self,Icon,x,y):
        self.Icon = Icon
        self.x = x
        self.y = y
    def getIcon(self):
        return self.Icon
    def getCoordinates(self):
        return [self.x,self.y]

class Wall(Objects):
    def __init__(self,x,y):
        super().__init__("#",x,y)

class Empty(Objects):
    def __init__(self,x,y):
        super().__init__(".",x,y)

class Item(Objects):
    def __init__(self,Icon,x,y):
        super().__init__(Icon,x,y)
    def PickUp(self):
        pass
class Bot(Objects):
    def __init__(self,state,x,y):
        super().__init__(self.state,x,y)



def createRightObject(Icon,x,y):
    if Icon == "#":
        return Wall(x,y)
    elif Icon == ".":
        return Empty(x,y)
    elif Icon == "^" or Icon == ">" or Icon == "v" or Icon == "<" or Icon == "o":
        return Bot(Icon,x,y)
    else:
        return Item(Icon,x,y)