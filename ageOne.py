import random
from const import*

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' # orange on some systems
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' # called to return to standard terminal text color

ageOneDictionary={
    "1":[3,"3","4"],
    "2":[3,"4","5"],
    "3":[3,"6","7"],
    "4":[3,"7","8"],
    "5":[3,"8","9"],
    "6":[3,"10","11"],
    "7":[3,"11","12"],
    "8":[3,"12","13"],
    "9":[3,"13","14"],
    "10":[3,"15","16"],
    "11":[3,"16","17"],
    "12":[3,"17","18"],
    "13":[3,"18","19"],
    "14":[3,"19","20"],
    "15":[1],
    "16":[1],
    "17":[1],
    "18":[1],
    "19":[1],
    "20":[1],
}


ageOneCards=["LumberYard","LoggingCamp","ClayPool","ClayPit","Quarry","StonePit","Glassworks","Press","GuardTower",
"WorkShop","Apothecary","StoneReserve","ClayReserve","WoodReserve","Stable","Garrison","Palisade","Scriptorium","Pharmacist",
"Theater","Altar","Baths","Tavern"]
gameAgeOneCards=[]
gameAgeOneCardsIsTurned=[False]*20
gameAgeOneCardsStacks=[]
gameAgeOneCardsIsPicked=[False]*20

minmax=[]
ComputerCards=[]
HumanCards=[]


def shuffleAgeOneCardsAndCreateStacks():
    global ageOneCards,gameAgeOneCards,gameAgeOneCardsStacks,gameAgeOneCardsIsTurned
    random.shuffle(ageOneCards)
    gameAgeOneCards=ageOneCards[:20]# εχω αφαιρέσει 3
    s11=gameAgeOneCards[:2]
    gameAgeOneCardsIsTurned[:2]=[True]*2
    s12=gameAgeOneCards[2:5]
    gameAgeOneCardsIsTurned[2:5]=[False]*3
    s13=gameAgeOneCards[5:9]
    gameAgeOneCardsIsTurned[5:9]=[True]*4
    s14=gameAgeOneCards[9:14]
    gameAgeOneCardsIsTurned[9:14]=[False]*5
    s15=gameAgeOneCards[14:20]
    gameAgeOneCardsIsTurned[14:20]=[True]*6
    gameAgeOneCardsStacks=[s11,s12,s13,s14,s15]

def switchPlayer():
    global currentPlayer
    if currentPlayer==Computer:
        currentPlayer=Human
    else:
        currentPlayer=Computer
def printAgeOneStack():
    check0sDict()
    counterOfCardsList=0                                 # a variable to run from 0 to 19 via loops and check  the lists we have for turned,picked.
    for i in range(0,len(gameAgeOneCardsStacks)):        # 0,1,2,3,4,
        for items in gameAgeOneCardsStacks[i]:           # for i =0 [pitsa souvlaki]---> items= pitsa souvlaki
            if gameAgeOneCardsIsTurned[counterOfCardsList]==False:
                print("XXX",end='   ')
            else:
                if(gameAgeOneCardsIsPicked[counterOfCardsList]==True):
                    print(RED,end='   ')
                    print(items,end='   ')
                    print(RESET,end='   ')
                else:
                    print(items,end='   ')
            counterOfCardsList+=1
        print()
        print()
    print("------------------------------------------")

def check0sDict():
    global gameAgeOneCardsIsTurned,minmax
    for i in range(0,20):
        if ageOneDictionary[str(i+1)][0]==1:
            gameAgeOneCardsIsTurned[i]=True
            minmax.append(i+1)
    print(min(minmax))

def newChoose():
    global gameAgeOneCardsIsPicked,minmax,ComputerCards,HumanCards
    notTakenYet=True
    while notTakenYet:
        #numberOfCardChoosen=int(input("choose a card from 1 to 20")) #xeirokinita me scanf
        numberOfCardChoosen=random.randint(min(minmax),max(minmax))   #dialegei mono toy tuxaia noumera
        if canTake(numberOfCardChoosen):# and gameAgeOneCardsIsPicked[numberOfCardChoosen-1]==False:
            ageOneDictionary[str(numberOfCardChoosen)][0]=0 # card is picked            
            gameAgeOneCardsIsPicked[numberOfCardChoosen-1]=True
            updateBounds(numberOfCardChoosen)
            notTakenYet=False
            if currentPlayer==Computer:
                ComputerCards.append(gameAgeOneCards[numberOfCardChoosen-1])
                print('Computer takes ',gameAgeOneCards[numberOfCardChoosen-1])
            else:
                HumanCards.append(gameAgeOneCards[numberOfCardChoosen-1])
                print('Human takes ',gameAgeOneCards[numberOfCardChoosen-1])
        


def canTake(cardNo):
    if ageOneDictionary[str(cardNo)][0] !=1:
        return False
    else:
        return True

def updateBounds(cardNo):
    global ageOneDictionary    
    for i in range(0,14):
        left=ageOneDictionary[str(i+1)][1]
        right=ageOneDictionary[str(i+1)][2]
        if left==str(cardNo) or right==str(cardNo):
            ageOneDictionary[str(i+1)][0]-=1
        

def roundAgeOne():
    shuffleAgeOneCardsAndCreateStacks()
    for i in range(0,20):
        printAgeOneStack()
        newChoose() #να αλλάξει το όνομα σε selectAgeOneCard()
        #decideAction() 
        switchPlayer()

#roundAgeOne()


def buildcard(card,currentPlayer):
     global HumanBank
     temp=[]
     canBuild=1
     if currentPlayer==Human:
        for i in range(0,9):
            if cardsDict["Age1"][gameAgeOneCards[card]][0][i]>HumanBank[i]:#if cost of card > human card
                canBuild=0
                ##a functions tha holds what we need to build this
        if canBuild:
            for i in range(0,len(HumanBank)):
                temp.append(cardsDict["Age1"][gameAgeOneCards[card]][1][i]+HumanBank[i])
        HumanBank=temp
        #HumanBank[10]-=cardsDict["Age1"][gameAgeOneCards[card]][0][8]
        



shuffleAgeOneCardsAndCreateStacks()
buildcard(2,Human)

print(HumanBank)








def decideForTrue(p): # p 0%->100%
    x=random.randint(0,100)
    return x<p


def decideAction(): # keep it(build), discard, build wonders
    if decideForTrue(50): #decide to keep it
        print('Player:',playerName[currentPlayer-1],' keeps the card')
    else:
        print('Player:',playerName[currentPlayer-1],' discards the card and earns 2coins')
        print('now has ',getMoney(),'coins')
        addMoney(currentPlayer,2)
        # να παραμείνει στη λίστα του παίκτη και να εισαχθεί στη λίστα των discard καρτών του
