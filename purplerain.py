import pygame, sys, random, time
from pygame.locals import *

FPS = 30
width = 1000
height = 700
scale = 250
cells = int((width + height)/2/scale)
drops = 2000
dropSpeed = 3
drift = 1 #wobbly deccent
driftChance = 4 #integer 1 - 10 = %
droph = -(height + scale)


#                      R    G    B      Opacity
BLACK   = (0, 0, 0)
PURPLE  = (110, 10, 90)
PURPLEFADE1  = (int(110*.80), int(10*.80), int(90*.80))
PURPLEFADE2  = (int(110*.66), int(10*.66), int(90*.66))
PURPLEFADE3  = (int(110*.33), int(10*.33), int(90*.33))

bgColor = BLACK

def main():
    global FPSClock, canvas, rain
    rain = []
    pygame.init()
    FPSClock = pygame.time.Clock()
    canvas = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Let it rain!")

    canvas.fill(bgColor)
    letitRain()
    
def drawRain(x,y,d):
    sizeDrop = cells/(drops/100)*d*2
    
    rain_alpha = pygame.Rect(x, y, sizeDrop, sizeDrop)
    pygame.draw.rect(canvas,PURPLE,rain_alpha)

    rain_beta = pygame.Rect(x, y-sizeDrop, sizeDrop, sizeDrop)
    pygame.draw.rect(canvas,PURPLEFADE1,rain_beta)

    rain_omega = pygame.Rect(x, y-sizeDrop*2, sizeDrop, sizeDrop)
    pygame.draw.rect(canvas,PURPLEFADE2,rain_omega)

    rain_delta = pygame.Rect(x, y-sizeDrop*3, sizeDrop, sizeDrop)
    pygame.draw.rect(canvas,PURPLEFADE3,rain_delta)

def initRain():
    for i in range(1,drops):
        raind = random.randrange(1,int(drops/100))
        if i <int(drops*.5):
            raind = random.randrange(1,int(drops/100*.4))
        elif i <int(drops*.65):
            raind = random.randrange(1,int(drops/100*.75))
        elif i <int(drops*.85):
            raind = random.randrange(1,int(drops/100*.85))
        else:
            raind = random.randrange(1,int(drops/100))
            
            
        rainx = random.randrange(0+cells,width-cells,cells)
        rainy = random.randrange(droph,0)
        drawRain(rainx,rainy,raind)
        rain.append([rainx,rainy,raind])

def moveRain():
    dropdrift = drift * cells
    for r, val in enumerate(rain):
        x, y, d = rain[r]
        speed = ((drops-(drops/5))/100)*dropSpeed/cells/(d)*2+dropSpeed
        if random.randrange(1,10) < driftChance:
            x = random.randrange(x - dropdrift,x + dropdrift)
        else:
            x = x
        if y >= height:
            y = random.randrange(droph,0)
            x = random.randrange(0+cells,width-cells,cells)
        if x > width or x < 0:
            x = random.randrange(0, width)
        rain[r] = [x,y + speed, d]
        drawRain(x,(y + speed), d)
    
        
    
def letitRain():
    
    initRain()
    print("Chance of precipitation = 100%")
    # letitRain loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                print("Rain god ED")
                pygame.quit()
                sys.exit()

        canvas.fill(bgColor)
        moveRain()
        pygame.display.update()
        FPSClock.tick(FPS)

main()

    
