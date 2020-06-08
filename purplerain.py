import pygame, sys, random, time, math
from pygame.locals import *

#                      R    G    B      Opacity

BLACK   = (10, 10, 10)
PURPLE  = (160, 10, 90)
PURPLEFADE1  = (int(160*.80), int(10*.80), int(90*.80),10)
PURPLEFADE2  = (int(160*.66), int(10*.66), int(90*.66),30)
PURPLEFADE3  = (int(160*.33), int(10*.33), int(90*.33),50)

Colors = [(0,255,0),(255,0,0),(0,0,255),(160, 10, 90),(255,255,0),(255,255,0),(255,0,255),(0,255,255)]

bgColor = BLACK

def main():

    global FPSClock, canvas, rain, scale, cells, drops, dropSpeed,drift,driftChance,droph,width,height,FPS
    global Color,ColorPall
    rain = []
    Color = []
    pygame.init()

    FPSClock = pygame.time.Clock()

    canvas = pygame.display.set_mode((1000,250))

    infoObject = pygame.display.Info()
    width = 1000
    height = 250
    print(width,height)
    FPS = 25 #Doubles as speed
    scale = 250
    cells = int((width + height)/2/scale)
    drops = 400
    dropSpeed = 4
    drift = 1 #wobbly deccent
    driftChance = 2 #integer 1 - 10 = %
    droph = -(height + scale)

    print(width,height)

    pygame.display.set_caption("Let it rain!")


    ColorPall = [random.choice(Colors) for x in range(1)]
    canvas.fill(bgColor)

    letitRain()

def drawRain(x,y,d,vx, tempColor):
    
    
    sizeDrop = cells/(drops/100)*d*2
    #pygame.draw.rect(canvas,PURPLE,(x+vx,y+int(random.uniform(-1,1 )),int(sizeDrop/2),sizeDrop))
    pygame.draw.rect(canvas,tempColor,(x+vx,y+int(random.uniform(-1,1 )),int(sizeDrop/2),sizeDrop))
   
def initRain():

    for i in range(1,drops):
        raind = random.randrange(1,int(drops/100))
        if i <int(drops*.5):
            raind = random.randrange(1,int(drops/100*.6))
        elif i <int(drops*.65):
            raind = random.randrange(1,int(drops/100*.75))
        elif i <int(drops*.85):
            raind = random.randrange(1,int(drops/100*.85))
        else:
            raind = random.randrange(1,int(drops/100))
        tempColor = random.choice(ColorPall)
        rainx = random.randrange(0+cells,width-cells,cells)
        rainy = random.randrange(droph,0)
        vx = random.uniform(-.2,.2)
        drawRain(rainx,rainy,raind,vx,tempColor)

        Color.append(tempColor)
        rain.append([rainx,rainy,raind,vx])

def moveRain(cl):

    dropdrift = drift * cells
    for r, val in enumerate(rain):
        x, y, d, vx = val
        speed = ((drops-(drops/5))/100)*dropSpeed/cells/(d)*2+dropSpeed
        if random.randrange(1,10) < driftChance:
            x = random.randrange(int(x - dropdrift),int(x + dropdrift))
        else:
            x = x
        if y >= height:
            y = random.randrange(droph,0)
            x = random.randrange(0+cells,width-cells,cells)
            vx = random.uniform(-1,1)

        if x > width+10 or x < 0-10:
            vx = random.uniform(-1,1)
            x = random.randrange(0, width)

        rain[r] = [x+vx,y + speed, d,vx]

        drawRain(x,(y + speed), d,vx,cl[r])

def letitRain():
    def trail():
        overlay = pygame.Surface(canvas.get_size())
        overlay.fill((0,0,0))
        overlay.set_alpha(25)
        canvas.blit(overlay,(0,0))
    ColorPall = [random.choice(Colors) for x in range(1)]
    
    Color = [random.choice(ColorPall) for x in range(drops)]
    initRain()

    print("Chance of precipitation = 100%")

    # letitRain loop

    while True:

        for event in pygame.event.get():

            if event.type==QUIT or pygame.key.get_pressed()[K_ESCAPE]:

                print("Rain god ED")

                pygame.quit()

                sys.exit()
            if pygame.key.get_pressed()[K_SPACE]:
                del Color
                ColorPall = [random.choice(Colors) for x in range(1)]
                Color = [random.choice(ColorPall) for x in range(len(rain)+1)]
                print("Color of rain changed to " + Color)

        #canvas.fill(bgColor)
        trail()
        moveRain(Color)
        pygame.display.update()
        FPSClock.tick(FPS)

main()

