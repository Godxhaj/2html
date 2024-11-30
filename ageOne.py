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
    for i in range(0,len(gameAgeOneCardsStacks)):        # 0,1,2,3,4,
        for items in gameAgeOneCardsStacks[i]:           # for i =0 [pitsa souvlaki]---> items= pitsa souvlaki
            if gameAgeOneCardsIsTurned[counterOfCardsList]==False:
                print(gp(5),"[-----]",end='   ')
            else:
                if(ageOneDictionary[str(i+1)][0]==Taken):
                    print(gp(5),RED,end='   ')
                    print(gp(5),items,end='   ')
                    print(gp(5),RESET,end='   ')
                elif(ageOneDictionary[str(counterOfCardsList+1)][0]==1):  # at ageOneDictionary( the 1st varible is 1==it means its available to be choosen)
                    print(gp(5),GREEN,end='  ')
                    print(gp(5),items,end='  ')
                    print(gp(5),RESET,end='  ')
                else:
                    print(gp(5),items,end='   ')                
            counterOfCardsList+=1
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
    ageOneDictionary[str(n)][0]=Taken

def allCardsAreTaken():
    cardsTaken=0
    for i in range(0,20):
        if ageOneDictionary[str(i+1)][0]==Taken:
            cardsTaken+=1
    print("   Cards Taken=",cardsTaken)
    return cardsTaken==20



def selectRandomlyAgeOneCard():
    i=0
    while(not allCardsAreTaken()):
        numberOfCardChoosen=random.randint(0,19) 
        #numberOfCardChoosen=int(input("give a card")) 
        if cardHasNoBounds(numberOfCardChoosen):
            return numberOfCardChoosen
        i+=1
        if i==10000:
            break
    return EndOfCards      

def getAgeOneCard():
    global ageOneDictionary
    numberOfCardToGet=selectRandomlyAgeOneCard()
    if numberOfCardToGet==EndOfCards:
        return EndOfCards
    ageOneDictionary[str(numberOfCardToGet+1)][0]=Taken
    leaseCardBounds(numberOfCardToGet)
    print('Player ',playerName[currentPlayer[0]],' has just got ',ageOneCards[numberOfCardToGet])
    return numberOfCardToGet


def leaseCardBounds(card):
    global ageOneDictionary
    for i in range (0,14):
        if ageOneDictionary[str(i+1)][1]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1
        if  ageOneDictionary[str(i+1)][2]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1



shuffleAgeOneCards()
getTwentyAgeOneCards()
createStack()
selectFirstPlayer()
# updateAndPrintAgeOneStack()
# getAgeOneCard()
# updateAndPrintAgeOneStack()
# getAgeOneCard()
# updateAndPrintAgeOneStack()
# getAgeOneCard()
# updateAndPrintAgeOneStack()
# updateAndPrintAgeOneStack()
# getAgeOneCard()
# updateAndPrintAgeOneStack()
# updateAndPrintAgeOneStack()
# getAgeOneCard()
# updateAndPrintAgeOneStack()

for i in range(0,20):
    updateAndPrintAgeOneStack()
    if getAgeOneCard()==EndOfCards:
        break
    switchPlayer()
print("End of Age One Cards!")

# ### ΤΕΡΑΣ!!! ###
# def selectAgeOneCard():
#     global gameAgeOneCardsIsPicked,playersCards
#     notTakenYet=True
#     while notTakenYet:        
#         numberOfCardChoosen=random.randint(0,19)   #dialegei mono toy tuxaia noumera
#         if cardHasNoBounds(numberOfCardChoosen):# and gameAgeOneCardsIsPicked[numberOfCardChoosen-1]==False:
#             setCardIsTaken(numberOfCardChoosen)
#             gameAgeOneCardsIsPicked[numberOfCardChoosen-1]=True
#             updateBounds(numberOfCardChoosen)
#             notTakenYet=False
#             playersCards[currentPlayer[0]].append(gameAgeOneCards[numberOfCardChoosen-1])
#             print(playerName[currentPlayer[0]]+' takes'+gameAgeOneCards[numberOfCardChoosen-1])
#             # if currentPlayer[0]==Computer:
#             #     ComputerCards.append(gameAgeOneCards[numberOfCardChoosen-1])
#             #     print('Computer takes ',gameAgeOneCards[numberOfCardChoosen-1])
#             # else:
#             #     HumanCards.append(gameAgeOneCards[numberOfCardChoosen-1])
#             #     print('Human takes ',gameAgeOneCards[numberOfCardChoosen-1])
        


# def canTake(cardNo):
#     if ageOneDictionary[str(cardNo)][0] !=1:
#         return False
#     else:
#         return True

# def updateBounds(cardNo):
#     global ageOneDictionary    
#     for i in range(0,14):
#         left=ageOneDictionary[str(i+1)][1]
#         right=ageOneDictionary[str(i+1)][2]
#         if left==str(cardNo) or right==str(cardNo):
#             ageOneDictionary[str(i+1)][0]-=1
        

# def roundAgeOne():
#     shuffleAgeOneCardsAndcreateStack()
#     for i in range(0,20):
#         printAgeOneStack()
#         selectAgeOneCard() #να αλλάξει το όνομα σε selectAgeOneCard()
#         #decideAction() 
#         switchPlayer()

# #roundAgeOne()


# def buildcard(card,currentPlayer):
#      global HumanBank
#      temp=[]
#      canBuild=1
#      if currentPlayer[0]==Human:
#         for i in range(0,9):
#             if cardsDict["Age1"][gameAgeOneCards[card]][0][i]>HumanBank[i]:#if cost of card > human card
#                 canBuild=0
#                 ##a functions tha holds what we need to build this
#         if canBuild:
#             for i in range(0,len(HumanBank)):
#                 temp.append(cardsDict["Age1"][gameAgeOneCards[card]][1][i]+HumanBank[i])
#         HumanBank=temp
#         #HumanBank[10]-=cardsDict["Age1"][gameAgeOneCards[card]][0][8]
        
# def newBuild(card):
#     city=[]
#     cost=((cardsDict["Age1"][gameAgeOneCards[card]][1]))  #cost of card in list
#     print(cost)
#     product=((cardsDict["Age1"][gameAgeOneCards[card]][2]))  #prod of card in list
#     for items in product:
#         city.append(items)
#     print(city)                  



# def keepcard(card):
#     global moneyOfComputer,moneyOfHuman
#     clear=1
#     playerNeeds=[]
#     compnothave=[]
#     cost=((cardsDict["Age1"][gameAgeOneCards[card]][1]))    #-->[coins,papyrus,...]
#     goods=((cardsDict["Age1"][gameAgeOneCards[card]][2])) 
#     for item in cost[1:]:
#         if item not in cityOfPlayer[currentPlayer[0]]:
#                 playerNeeds.append(item)
#                 clear=0
#         if clear and cost[0]<=coins[currentPlayer[0]]:
#             print('You can build that card!')
#             coins[currentPlayer[0]]-=cost[0]
#             for i in range(1,len(goods)):
#                 cityOfPlayer[currentPlayer[0]].append(goods[i])
#                 coins[currentPlayer[0]]+=goods[0]
#         else:
#             print('you cannot build that!')
#             print('you need to buy',playerNeeds[currentPlayer[0]])


    
    
 



# print('666 ',currentPlayer[0])
# print(cityOfPlayer[currentPlayer[0]])
# chooseFirstPlayer()
# shuffleAgeOneCardsAndcreateStack()
# keepcard(2)
# print(gameAgeOneCards[2])
# print(coins[0])
# print(coins[1])
# print('666 ',currentPlayer[0])
# print(cityOfPlayer[currentPlayer[0]])

# '''
# shuffleAgeOneCardsAndcreateStack()
# print(gameAgeOneCards)
# newBuild(2)
# '''







# def decideForTrue(p): # p 0%->100%
#     x=random.randint(0,100)
#     return x<p


# def decideAction(): # keep it(build), discard, build wonders
#     if decideForTrue(50): #decide to keep it
#         print('Player:',playerName[currentPlayer[0]-1],' keeps the card')
#     else:
#         print('Player:',playerName[currentPlayer[0]-1],' discards the card and earns 2coins')
#         print('now has ',getMoney(),'coins')
#         addMoney(currentPlayer[0],2)
#         # να παραμείνει στη λίστα του παίκτη και να εισαχθεί στη λίστα των discard καρτών του
