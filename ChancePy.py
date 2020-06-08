import random
from pickle import load,dump

def what(obj, callingLocals=locals()):
    """
    returns variable name as a string   
    """
    for k, v in list(callingLocals.items()):
         if v is obj:
            name = k
            return name

class die:
    def __init__(self):
        self.Data = []
    def roll(self, sides,startat = 0):
        random.seed()
        return random.randrange(startat,sides + startat)
    def chance(self, threshold):
        random.seed()
        if random.random() >= threshold:
            return True
        else:
            return False
    def throw(self, dice, sides,startat = 0):
        random.seed()
        Resaults = []
        for x in range(0,dice):
            Resaults.append(self.roll(sides,startat))
        return Resaults
    def color(self,Transpartent = False, Alpha = - 1):
        if Transpartent == False:
            colors = (random.randrange(0,255),
                random.randrange(0,255),
                random.randrange(0,255))
        else:
            if Alpha > -1:
                colors = (random.randrange(0,255),
                    random.randrange(0,255),
                    random.randrange(0,255),
                    Alpha)
            else:
                colors = (random.randrange(0,255),
                    random.randrange(0,255),
                    random.randrange(0,255),
                    random.randrange(0,255))

        return colors
    def create_preset(self, throwData):
        #each Data set = [dice,sides,startat]
        self.Data += throwData
    def throw_preset(self,die_number):
        dice,sides,startat = self.Data[die_number]
        return self.throw(dice,sides,startat)



class bottle:
    def __init__(self,MasterFile,ext = ".p"):
        self.MasterFile = str(MasterFile) + ext
    def cork(self,object):
        dump(object,open(self.MasterFile,'wb'))
    def uncork(self):
        return load(open(self.MasterFile,'rb'))
    def label(self):
        return str(self.MasterFile)

class chest:

    def __init__(self,bottles = []):
        #bottles = list of file names
        if bottles != []:
            self.bottles = [bottle(x) for x in bottles]
            self.summon = {str(x):bottle(x) for x in bottles}
        else:
            self.bottles = []
            self.summon = {}
    def labels(self,arg = - 1):
        #to return all lables do not pass an arg
        if arg > -1:
            return self.bottles[arg].label()
        else:
            jugs = []
            jugs = [x.label() for x in self.bottles]
            return jugs
    def addBottle(self,bottles = []):
        self.bottles += [bottle(x) for x in bottles]
        self.summon.update({str(x):bottle(x) for x in bottles})
    def delBottle(self,BottleIndex = []):
        print("chest.delBottle = WIP")

    def vault(self):
        bottle(what(self),".pChest").cork(self)
    def unvault(self):
        handshake = bottle(self.bottles[0].label().split('.')[0],".pChest").uncork()
        return handshake
