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

def gp(n):
    str=""
    for i in range(0,n):
        str+=" "
    return str

def printGameStartLogo():
    print(RED,'****************************')
    print(GREEN,'* 7Wonder DUEL STARTS!!!   *')
    print(GREEN,'*     by C.G 2024          *')
    print(CYAN,'****************************',RESET)

def getRand(pdf): #return 0,1,2,..,length(pdf)-1
    n=random.randint(0,100)   
    sum=0
    for i in range(0,len(pdf)): # i=1,2,3
        if n<pdf[i]+sum:
            return i+1
        sum+=pdf[i]
    return -1
