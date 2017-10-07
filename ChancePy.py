import random
 
class die:
    def __init__(self):
        self.Data = []
    def check_seed(self):
        random.seed()
    def roll(self, sides):
        self.check_seed()
        return random.randrange(1,sides)
    def sroll(self, sides):
        self.check_seed()
        return random.randrange(0,sides)
    def chance(self, threshold):
        self.check_seed()
        if random.random() <= threshold:
            return True
        else:
            return False
    def throw(self, dice, sides):
        self.check_seed()
        Resaults = []
        for x in range(0,dice):
            Resaults.append(self.roll(sides))
        return Resaults
    def color(self):
        self.check_seed()
        color_picker = (random.randrange(0,255),
            random.randrange(0,255),
            random.randrange(0,255))
        return color_picker
    def selector(self,array):
        self.check_seed()
        return random.choice(array)