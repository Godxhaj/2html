import random
from const import *
from colors import *
from wonderCards import *
from mainFunctions import *
roundOneWonderCardsPicked=[False]*4
roundTwoWonderCardsPicked=[False]*4
wonderCardsPicked=[roundOneWonderCardsPicked,roundTwoWonderCardsPicked]
gameWonderCards=[[],[]]



def shuffleWonderCards(): #shuffles wonderCards and gives 2  4card-lists for the 2 rounds
    global wonderCards,gameWonderCards,roundOneWonderCards,roundTwoWonderCards
    random.shuffle(wonderCards)
    gameWonderCards[0]=wonderCards[:4]             
    gameWonderCards[1]=wonderCards[4:8]             
    roundOneWonderCards=wonderCards[:4]
    roundTwoWonderCards=wonderCards[4:8]

def printWonderCardsNames(round):
    str=""
    for i in range(0,4):
        if wonderCardsPicked[round][i]==False:
            str+=RED +gameWonderCards[round][i]+' '+RESET
        else:
            str+=CYAN + gameWonderCards[round][i]+' '+RESET
    print(str)


# def printValuesOfDicRoundTwo(i):#kolpo gia na ginei lista "string"
#     stri=list(wonderCostDict[roundTwoWonderCards[i]])
#     return str(stri)

# def printValuesOfDicRoundOne(i):#kolpo gia na ginei lista "string"
#     stri=list(wonderCostDict[roundOneWonderCards[i]])
#     return str(stri)

def canPicked(round,numberOfCard):
    return not wonderCardsPicked[round][numberOfCard]


def cardIsPicked(round,numberOfCard):
    global wonderCardsPicked
    wonderCardsPicked[round][numberOfCard]=True


def chooseWonderCard(round,numberOfCardsToSelect):
    global playerWonders
    count=numberOfCardsToSelect
    while(count!=0):
        card=random.randint(0,3)        
        if(canPicked(round,card)): #πρεπει να τραβηξουμε της σωστης λιστας το στοιχείο
            cardIsPicked(round,card)
            count-=1
            playerWonders[currentPlayer[0]].append(gameWonderCards[round][card])            
            print('Player:',playerName[currentPlayer[0]],' choose ',gameWonderCards[round][card])

def playWonder():
    #selectFirstPlayer()
    shuffleWonderCards()
    playWonderRound(roundOne)
    playWonderRound(roundTwo)
    printPlayersWonderCards()

def playWonderRound(round):
    numberOfCardsToSelect=[1,2,1]
    for i in numberOfCardsToSelect:
        chooseWonderCard(round,i)
        switchPlayer()


def printPlayersWonderCards():
    print(RED+'Computer:', playerWonders[0],RESET)
    print(CYAN+'Human:', playerWonders[0],RESET)

#playWonder()






def playersSelectWonders():
    shuffleWonderCards()
    print("Welcome to the 7 Wonders duel")    
    print("player" +str(currentPlayer[0])+ "choose one Wonder")
    roundOneWonders()
    switchPlayer()
    roundTwoWonders()
    print("human--->" + str(humanWonders))
    print("computer--->"+str(computerWonders))


#gameStarts()