import random
from const import*
from colors import *
from ageCards import *
from mainFunctions import *

def shuffleAgeOneCards():
    global ageOneCards
    random.shuffle(ageOneCards)

def getTwentyAgeOneCards():
    global gameAgeOneCards
    gameAgeOneCards=ageOneCards[:20]# επιλέγουμε τις 20 πρώτες κάρτες μετά το ανακάτεμα


def createStack(): #ok
    global gameAgeOneCardsStacks,gameAgeOneCardsIsTurned    
    gameAgeOneCardsStacks=[gameAgeOneCards[:2],gameAgeOneCards[2:5],gameAgeOneCards[5:9],gameAgeOneCards[9:14],gameAgeOneCards[14:20]]
    gameAgeOneCardsIsTurned[:2]=[True]*6
    gameAgeOneCardsIsTurned[2:5]=[False]*3
    gameAgeOneCardsIsTurned[5:9]=[True]*4
    gameAgeOneCardsIsTurned[9:14]=[False]*5
    gameAgeOneCardsIsTurned[14:20]=[True]*6





def cardHasNoBounds(n):
    return ageOneDictionary[str(n+1)][0]==NoBounds    
def turnCard(n):
    gameAgeOneCardsIsTurned[n]=True




def updateStateOfCards(): # ανανεώνει ενδεχόμενη κατάσταση επιλογής κάρτας
    global gameAgeOneCardsIsTurned,minmax
    for i in range(0,20):
        if cardHasNoBounds(i):
            turnCard(i)



def updateAndPrintAgeOneStack(): #ok
    updateStateOfCards()
    print(YELLOW,"+--------  AGE ONE STACK  ------------------------+",RESET)
    counterOfCardsList=0                                 # a variable to run from 0 to 19 via loops and check  the lists we have for turned,picked.
    gap=[33,24,15,6,0]
    line=0
    for i in range(0,len(gameAgeOneCardsStacks)):        # 0,1,2,3,4,
        print(gp(gap[line]),end=' ')
        for items in gameAgeOneCardsStacks[i]:           # for i =0 [pitsa souvlaki]---> items= pitsa souvlaki             
            if gameAgeOneCardsIsTurned[counterOfCardsList]==False:
                print("[-----------]",end='   ')
            else:
                #if(ageOneDictionary[str(i+1)][0]==Taken):
                if(ageOneDictionary[str(counterOfCardsList+1)][0]==Taken):
                    print(RED,end=' ')
                    print(items,end=' ')
                    print(RESET,end=' ')
                elif(ageOneDictionary[str(counterOfCardsList+1)][0]==Available):  # at ageOneDictionary( the 1st varible is 1==it means its available to be choosen)
                    print(GREEN,end=' ')
                    print(items,end=' ')
                    print(RESET,end=' ')
                else:
                    print(items,end=' ')                
            counterOfCardsList+=1
        line+=1
        print()
        print()
    print(YELLOW,"+------------------------------------------+",RESET)


def playAgeOne():
    shuffleAgeOneCards() # ανακατεύονται όλες οι κάρτες
    getTwentyAgeOneCards() #επιλέγονται 20 κάρτες από τις 23
    createStack() # 
    updateAndPrintAgeOneStack()

def setCardIsTaken(n):
    global ageOneDictionary
    ageOneDictionary[str(n+1)][0]=Taken

def allCardsAreTaken():
    cardsTaken=0
    for i in range(0,20):
        if ageOneDictionary[str(i+1)][0]==Taken:
            cardsTaken+=1
    #print("   Cards Taken=",cardsTaken)
    return cardsTaken==20



def selectRandomlyAgeOneCard():
    i=0
    while(not allCardsAreTaken()):
        numberOfCardChoosen=random.randint(0,19)         
        if cardHasNoBounds(numberOfCardChoosen):
            return numberOfCardChoosen
        i+=1
        if i==10000:
            break
    return EndOfCards      

def scoreAvailableCards():
    # η μέθοδος θα σκοράρει κάθε κάρτα που είναι διαθέσιμη με κριτήρια: κόστος,υλικά,χρώμα, δίνοντας κατάλληλη τιμή 
    #βάρους στο κάθε κριτήριο από 0,....1
    print()

def lookAtColorOfCard(card):
    color=cardsDict["Age1"][gameAgeOneCards[card]][0]
    return color # return the color with its value not by name

def lookAtCostOfCard(card):
    cost=cardsDict["Age1"][gameAgeOneCards[card]][1]
    return cost

def lookAtGoodsOfCard(card):
    goods=cardsDict["Age1"][gameAgeOneCards[card]][2]
    return goods

def evaluateColor(color):
    prioList=[Green,Gold,Red,Blue,Brown,Grey]
    return prioList.index(color) +1 #return the index of prio col.[1-7]

def evaluateCost(cost):
    coinsCost=cost[0]# returns the coins of the cost list
    return coinsCost #0,1,2,3

def evaluateTheCard(card):
    a=[2,1]
    cost=lookAtCostOfCard(card)
    color=lookAtColorOfCard(card)
    goods=lookAtGoodsOfCard(card)
    # evaluateGoods(goods)
    finalScore=evaluateColor(color)/7*a[0]-evaluateCost(cost)/7*a[1]
    return finalScore



def playerDecidesActionForAgeOneCard(number):
    actionPDF=[40,40,20]
    #actionForFreeCard=[95,5]
    action=getRand(actionPDF)+actionOffset
    return action

def playerActs(action,card):
    if action==BuildBuilding:
        playerBuildsBuilding(card)
    elif action==Discard:
        playerDiscardsCard(card)
    else:
        playerBuildsWonder(card)

def getAgeOneCard():
    global ageOneDictionary
    numberOfCardToGet=selectRandomlyAgeOneCard()
    if numberOfCardToGet==EndOfCards:
        return EndOfCards
    setCardIsTaken(numberOfCardToGet)
    releaseCardBounds(numberOfCardToGet)
    print('Player ',playerName[currentPlayer[0]],' has ',ageOneCards[numberOfCardToGet],' and decides...') 
    return numberOfCardToGet


def playerBuildsBuilding(card): #for card =free money,no  check if its possible
    global cityOfPlayer
    cityOfPlayer[currentPlayer[0]].extend(cardsDict["Age1"][gameAgeOneCards[card]][2])  
    print(GREEN,playerName[currentPlayer[0]],"builds building and from now on has " ,*cityOfPlayer[currentPlayer[0]],"in his city",RESET)         

def playerDiscardsCard(card):
    print(RED,playerName[currentPlayer[0]]," discards the Age One card",RESET)

def playerBuildsWonder(card):
    print(YELLOW,playerName[currentPlayer[0]]," builds wonder",RESET)


def releaseCardBounds(card):
    global ageOneDictionary
    for i in range (0,14):
        if ageOneDictionary[str(i+1)][1]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1
        if  ageOneDictionary[str(i+1)][2]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1



os.system('cls')

def playAgeOneGame():
    shuffleAgeOneCards()
    getTwentyAgeOneCards()
    createStack()
    selectFirstPlayer()
    for i in range(0,20):
        updateAndPrintAgeOneStack()
        numberOfCardToGet=getAgeOneCard()
        if numberOfCardToGet==EndOfCards:
            break        
        action=playerDecidesActionForAgeOneCard(numberOfCardToGet)        
        playerActs(action,numberOfCardToGet)
        switchPlayer()
    print("End of Age One Cards!")

playAgeOneGame()
#lookAtColorOfCard(2)
#print(lookAtCostOfCard(2))
# evaluateTheCard(2)
a=[]
for i in range(0,len(gameAgeOneCards)):
    #print(gameAgeOneCards[i],end=' ')
    z=[gameAgeOneCards[i],evaluateTheCard(i)]
    a.append(z)

print("+++++++++++++")
a_sorted = sorted(a, key=lambda x: x[1])

for row in a_sorted:
    print(row)