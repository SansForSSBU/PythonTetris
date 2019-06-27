#importing modules
import pygame
import math
import random
import time
random.seed(time.time())
pygame.font.init()
pygame.mixer.init()
#getting music
ThemeA=pygame.mixer.music.load("Music/ThemeA.ogg")
#getting images, pygame goes down from parent directory
cyanBlock=pygame.image.load("Blocks/cyanblock.png")#1
blueBlock=pygame.image.load("Blocks/blueblock.png")#2
greenBlock=pygame.image.load("Blocks/greenblock.png")#3
orangeBlock=pygame.image.load("Blocks/orangeblock.png")#4
purpleBlock=pygame.image.load("Blocks/purpleblock.png")#5
redBlock=pygame.image.load("Blocks/redblock.png")#6
yellowBlock=pygame.image.load("Blocks/yellowblock.png")#7
Tetrad1=pygame.image.load("Tetrads/linehorizontal.png")#1, line piece
Tetrad2=pygame.image.load("Tetrads/Lpiece.png")#2, L piece
Tetrad3=pygame.image.load("Tetrads/Spiece.png")#3, S piece
Tetrad4=pygame.image.load("Tetrads/Jpiece.png")#4, J piece
Tetrad5=pygame.image.load("Tetrads/Tpiece.png")#5, T piece
Tetrad6=pygame.image.load("Tetrads/Zpiece.png")#6, Z piece
Tetrad7=pygame.image.load("Tetrads/Squarepiece.png")#7, Square piece
tetradTable=[Tetrad1,Tetrad2,Tetrad3,Tetrad4,Tetrad5,Tetrad6,Tetrad7]
blockTable=[cyanBlock,blueBlock,greenBlock,orangeBlock,purpleBlock,redBlock,yellowBlock]
#functions are defined here
def drawGrid():#this will draw the grid, not render the blocks
    for i in range(columns+1):
        X=drawBoundsX[0]+i*drawIncX
        pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]),(X,drawBoundsY[0],lineWidth,drawLenY))
    for i in range(rows+1):
        Y=drawBoundsY[0]+i*drawIncY
        pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]),(drawBoundsX[0],Y,drawLenX,lineWidth))
def drawSquare(x,y,colour):
    win.blit(blockTable[colour-1],(x*25+drawBoundsX[0]+1,y*25+drawBoundsY[0]+1))
def drawSquares():#colour support will need to be coded in by changing table from bools to numbers, with numbers representing colours
    for i in range(200):
        if grid[i]!=0:
            Y=math.floor(i/10)
            X=i-Y*10
            drawSquare(X,Y,grid[i])
def drawNext():
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,26,2,300))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,26,150,2))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,326,150,2))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (450,26,2,300))
    win.blit(textbox,(310,30))
    win.blit(tetradTable[nextSequence[0][0]-1],(310,80))
    win.blit(tetradTable[nextSequence[1][0]-1],(310,150))
    win.blit(tetradTable[nextSequence[2][0]-1],(310,230))
def startBlockFalling():
    global nextSequence
    global fallerType
    global fallerOrientation
    global fallerX
    global fallerY
    fallerType=nextSequence[0][0]
    fallerOrientation=nextSequence[0][1]
    fallerY=1
    fallerX=3
    nextSequence[0]=nextSequence[1]
    nextSequence[1]=nextSequence[2]
    nextSequence[2]=[random.randint(1,7),random.randint(1,4)]
def getFallerBlocks(fallerOrientation,fallerType):#DOWN IS POSITIVE, RIGHT IS POSITIVE. final "else" is an error handler.
    if fallerType==1:#Line
        if fallerOrientation==1:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX+1,fallerY],[fallerX+2,fallerY]]
        elif fallerOrientation==2:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX,fallerY+2]]
        elif fallerOrientation==3:
            return [[fallerX-2,fallerY],[fallerX-1,fallerY],[fallerX,fallerY],[fallerX+1,fallerY]]
        elif fallerOrientation==4:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX,fallerY+2]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==2:#L
        if fallerOrientation==1:
            return [[fallerX-1,fallerY],[fallerX-1,fallerY-1],[fallerX,fallerY],[fallerX+1,fallerY]]
        elif fallerOrientation==2:
            return [[fallerX,fallerY+1],[fallerX,fallerY],[fallerX,fallerY-1],[fallerX+1,fallerY-1]]
        elif fallerOrientation==3:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX+1,fallerY],[fallerX+1,fallerY+1]]
        elif fallerOrientation==4:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX-1,fallerY+1]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==3:#S
        if fallerOrientation==1:
            return [[fallerX-1,fallerY+1],[fallerX,fallerY+1],[fallerX,fallerY],[fallerX+1,fallerY]]
        elif fallerOrientation==2:
            return [[fallerX-1,fallerY-1],[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY+1]]
        elif fallerOrientation==3:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY-1],[fallerX+1,fallerY-1]]
        elif fallerOrientation==4:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX+1,fallerY],[fallerX+1,fallerY+1]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==4:#J
        if fallerOrientation==1:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX+1,fallerY],[fallerX+1,fallerY-1]]
        elif fallerOrientation==2:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX+1,fallerY+1]]
        elif fallerOrientation==3:
            return [[fallerX-1,fallerY+1],[fallerX-1,fallerY],[fallerX,fallerY],[fallerX+1,fallerY]]
        elif fallerOrientation==4:
            return [[fallerX-1,fallerY-1],[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==5:#T
        if fallerOrientation==1:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY-1],[fallerX+1,fallerY]]
        elif fallerOrientation==2:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX+1,fallerY]]
        elif fallerOrientation==3:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX+1,fallerY]]
        elif fallerOrientation==4:
            return [[fallerX,fallerY-1],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX-1,fallerY]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==6:#Z
        if fallerOrientation==1:
            return [[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY+1],[fallerX+1,fallerY+1]]
        elif fallerOrientation==2:
            return [[fallerX-1,fallerY+1],[fallerX-1,fallerY],[fallerX,fallerY],[fallerX,fallerY-1]]
        elif fallerOrientation==3:
            return [[fallerX-1,fallerY-1],[fallerX,fallerY-1],[fallerX,fallerY],[fallerX+1,fallerY]]
        elif fallerOrientation==4:
            return [[fallerX,fallerY+1],[fallerX,fallerY],[fallerX+1,fallerY],[fallerX+1,fallerY-1]]
        else:
            return [[fallerX,fallerY]]
    if fallerType==7:#Square
        return [[fallerX,fallerY],[fallerX,fallerY-1],[fallerX+1,fallerY],[fallerX+1,fallerY-1]]
def getBlock(x,y,gridType):#gridType=True: "get from the actual grid", otherwise: "get from this grid i gave you"
    if x+y*10<200 and x<10 and x>=0:#check if coords are outside the grid
        if gridType==True:
            return grid[x+y*10]
        else:
            return gridType[x+y*10]
    else:
        return 8#8 means "outside the box"
def setBlock(x,y,colour):
    global score
    global grid
    if x+y*10<200:
        grid[x+y*10]=colour
def drawFaller():
    for i in getFallerBlocks(fallerOrientation,fallerType):
        drawSquare(i[0],i[1],fallerType)
def dropFaller():
    global score
    global fallerY
    global placeTimer
    CannotDrop=False
    for i in getFallerBlocks(fallerOrientation,fallerType):
        if getBlock(i[0],i[1]+1,True)!=0:
            CannotDrop=True
    if not CannotDrop:
        fallerY+=1
        placeTimer=0
        if pressed[pygame.K_DOWN]:
            score+=1
    else:
        if placeTimer>=placeDelay:
            placeFaller()
            startBlockFalling()
            return True
        else:
            placeTimer+=1
    return False
def clearLines(Y):
    global grid
    global lines
    global score
    clearYs=[]
    for i in Y:
        canClear=True
        for j in range(10):
            if getBlock(j,i,True)==0:
                canClear=False
        if canClear:
            if not i in clearYs:
                clearYs.append(i)
    if len(clearYs)>0:
        dropYs=[]
        for i in range(20):
            dropYs.append(0)
        for i in clearYs:
            lines+=1
            score+=100
            for j in range(10):
                setBlock(j,i,0)
            for k in range(i):
                dropYs[k]=dropYs[k]+1
        gridcopy=grid
        for i in range(20)[::-1]:#Y
            fallY=dropYs[i]
            for j in range(10):#X
                if i-fallY>=0:
                    setBlock(j,i+fallY,getBlock(j,i,gridcopy))
def placeFaller():
    global canHold
    Y=[]
    for i in getFallerBlocks(fallerOrientation,fallerType):
        setBlock(i[0],i[1],fallerType)
        if not i[1] in Y:
            Y.append(i[1])
    clearLines(Y)
    checkFailure()
    canHold=True
def moveRight():
    global fallerX
    canMove=True
    for i in getFallerBlocks(fallerOrientation,fallerType):
        if not getBlock(i[0]+1,i[1],True)==0:
            canMove=False
    if canMove:
        fallerX+=1
def moveLeft():
    global fallerX
    canMove=True
    for i in getFallerBlocks(fallerOrientation,fallerType):
        if not getBlock(i[0]-1,i[1],True)==0:
            canMove=False
    if canMove:
        fallerX+=-1
def rotate(direction):#True=Clockwise, False=Anticlockwise
    global fallerOrientation
    global fallerX
    global fallerY
    if direction:
        if fallerOrientation==4:
            newOrientation=1
        else:
            newOrientation=fallerOrientation+1
    else:
        if fallerOrientation==1:
            newOrientation=4
        else:
            newOrientation=fallerOrientation-1
    blocks=getFallerBlocks(newOrientation,fallerType)
    easyrotate=True
    conflictBlocks=[]
    for i in blocks:
        if not getBlock(i[0],i[1],True)==0:
            easyrotate=False
            conflictBlocks.append(i)
    if easyrotate:
        fallerOrientation=newOrientation
    else:
        #if the core doesn't phase, the block doesn't phase
        conflictXneg=0
        conflictXpos=0
        conflictYneg=0
        conflictYpos=0
        for i in conflictBlocks:#conflict can't be in the centre
            if i[0]<fallerX:
                conflictXneg+=1
            elif i[0]>fallerX:
                conflictXpos+=1
            if i[1]<fallerY:
                conflictYneg+=1
            elif i[1]>fallerY:
                conflictYpos+=1
        AllowRotate=True
        if fallerType==1:#this is needed in case a line piece is rotated and there's a 1 block thick wall. it needs to be pushed 2 to the side by this wall under some circumstances.
            if newOrientation==1:
                if conflictXpos==1:
                    for i in conflictBlocks:
                        if [i[0]+1,i[1]] in blocks and not i==[fallerX,fallerY]:
                            conflictXpos=2
            elif newOrientation==2:
                if conflictYpos==1:
                    for i in conflictBlocks:
                        if [i[0],i[1]+1] in blocks and not i==[fallerX,fallerY]:
                            conflictYpos=2
            elif newOrientation==3:
                if conflictXneg==1:
                    for i in conflictBlocks:
                        if [i[0]-1,i[1]] in blocks and not i==[fallerX,fallerY]:
                            conflictXneg=2
            elif newOrientation==4:
                if conflictYneg==1:
                    for i in conflictBlocks:
                        if [i[0],i[1]-1] in blocks and not i==[fallerX,fallerY]:
                            conflictYneg=2       
        for i in blocks:
            if not getBlock(i[0]+conflictXneg-conflictXpos,i[1]+conflictYneg-conflictYpos,True)==0:
                AllowRotate=False
        if AllowRotate:
            fallerOrientation=newOrientation
            fallerX+=conflictXneg-conflictXpos
            fallerY+=conflictYneg-conflictYpos
def hold():
    global canHold
    global heldType
    global heldOrientation
    global fallerType
    global fallerOrientation
    global nextSequence
    global fallerY
    global fallerX
    if canHold:
        canHold=False
        if heldType==0:
            heldType=fallerType
            heldOrientation=fallerOrientation
            startBlockFalling()
        else:
            holdt=fallerType
            holdo=fallerOrientation
            fallerType=heldType
            fallerOrientation=heldOrientation
            heldType=holdt
            heldOrientation=holdo
            fallerY=1
            fallerX=3
def hardDrop():
    global score
    global fallerY
    while True:
        currY=fallerY
        if dropFaller():
            break
        elif not currY==fallerY:
            score+=2#harddrop bonus
def drawHold():
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,350,2,175))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,350,150,2))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (300,525,150,2))
    pygame.draw.rect(win,(gridColourRGB[0],gridColourRGB[1],gridColourRGB[2]), (450,350,2,175))
    win.blit(textbox2,(310,360))
    if heldType!=0:
        win.blit(tetradTable[heldType-1],(310,420))
        
def drawScore():
    win.blit(textbox3,(50,600))
    win.blit(textbox4,(300,600))
def drawFailureLine():
    pygame.draw.rect(win,(255,0,0),(26,126,250,lineWidth))
def checkFailure():
    global grid
    global run
    for i in range(40):
        if not grid[i]==0:
            run=False
#notes:
#tetris has 10 columns and 20 rows. the table will go along the rows, then down a row each time
#tetrominoes will be assigned numbers based on the order shown in the image at https://tetris.fandom.com/wiki/Tetromino

#variables important to game are setup here
columns=10
rows=20
gridColourRGB=[60,60,60]
textColourRGB=[100,100,100]
lineWidth=1
drawBoundsX=[26,276]
drawBoundsY=[26,526]
defaultSquareColour=[255,0,0]
font=pygame.font.SysFont("Times New Roman",30)
bgColour=[0,0,0]
debug=True
#implied
drawLenX=drawBoundsX[1]-drawBoundsX[0]
drawLenY=drawBoundsY[1]-drawBoundsY[0]
drawIncX=drawLenX/columns
drawIncY=drawLenY/rows
textbox=font.render("NEXT",False,(textColourRGB[0],textColourRGB[1],textColourRGB[2]))
textbox2=font.render("HOLD",False,(textColourRGB[0],textColourRGB[1],textColourRGB[2]))
#dont change
canHold=True
score=0
lines=0
heldType=0
heldOrientation=0
fallerType=0
fallerOrientation=0
fallerX=0
fallerY=0
fallerTimer=0
fallerBaseDelay=0.5
fallerDelay=0.5
minBaseDelay=0.1
difficultySpeed=0.00001#how fast the difficulty increases per tick
placeTimer=0
placeDelay=3#this is how many times it would have to be placed without the place delay code +1, to be placed.
Righttimer=0
Lefttimer=0
Movetimer=0.4
nextSequence=[[random.randint(1,7),random.randint(1,4)],[random.randint(1,7),random.randint(1,4)],[random.randint(1,7),random.randint(1,4)]]
grid=[]
for i in range(200):
    grid.append(0)
#window starts here
pygame.init()
win=pygame.display.set_mode((500,700))
pygame.display.set_caption("Tetris")
run=True
pygame.mixer.music.play(-1,0)
startBlockFalling()
while run:
    pygame.time.delay(50)#0.05sec ticks
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN and event.key==pygame.K_w:
            rotate(True)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_s:
            rotate(False)
        if event.type==pygame.KEYDOWN and event.key==pygame.K_h:
            hold()
        if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
            hardDrop()
    win.fill((bgColour[0],bgColour[1],bgColour[2]))
    textbox3=font.render("SCORE:"+str(score),False,(textColourRGB[0],textColourRGB[1],textColourRGB[2]))
    textbox4=font.render("LINES:"+str(lines),False,(textColourRGB[0],textColourRGB[1],textColourRGB[2]))
    drawGrid()
    drawSquares()
    drawNext()
    drawFaller()
    drawHold()
    drawScore()
    drawFailureLine()
    pygame.display.update()
    if fallerTimer>=fallerDelay:
        fallerTimer=0
        dropFaller()
    fallerTimer+=0.05
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        fallerDelay=fallerBaseDelay/4
    else:
        fallerDelay=fallerBaseDelay
    if pressed[pygame.K_d] and not pressed[pygame.K_a]:
        if Righttimer==0:
            moveRight()
        Righttimer+=0.05
    elif pressed[pygame.K_a] and not pressed[pygame.K_d]:
        if Lefttimer==0:
            moveLeft()
        Lefttimer+=0.05
    else:
        Righttimer=0
        Lefttimer=0
    if Righttimer>0 and Lefttimer>0:
        if Righttimer>Lefttimer:
            Righttimer=Righttimer-Lefttimer
            Lefttimer=0
        elif Lefttimer>Righttimer:
            Lefttimer=Lefttimer-Righttimer
            Righttimer=0
        else:
            Righttimer=0
            Lefttimer=0
    if Righttimer>=Movetimer:
        moveRight()
        Righttimer=0.01
    elif Lefttimer>=Movetimer:
        moveLeft()
        Lefttimer=0.01
    if not pressed[pygame.K_d]:
        Righttimer=0
    if not pressed[pygame.K_a]:
        Lefttimer=0
    if fallerBaseDelay>minBaseDelay:
        fallerBaseDelay=fallerBaseDelay-difficultySpeed
    
