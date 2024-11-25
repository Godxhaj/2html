import random
from const import *


def selectFirstPlayer():
    global currentPlayer
    currentPlayer[0]=random.randint(0,1)

def switchPlayer():
    global currentPlayer
    if currentPlayer[0]==Computer:
        currentPlayer[0]=Human
    else:
        currentPlayer[0]=Computer


def printGameStartLogo():
    print(RED,'****************************')
    print(GREEN,'* 7Wonder DUEL STARTS!!!   *')
    print(GREEN,'*     by C.G 2024          *')
    print(CYAN,'****************************',RESET)
