import random
currentPlayer=0
humanWonders=[]
computerWonders=[]
Noboby,Computer,Human,Burned=0,1,2,3


def chooseFirstPlayer():
    global currentPlayer
    currentPlayer=random.randint(1,2)
def switchPlayer():
    global currentPlayer
    if currentPlayer==Computer:
        currentPlayer=Human
    else:
        currentPlayer=Computer