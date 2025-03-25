import random
from const import*
from colors import *
from ageCards import *
from mainFunctions import *
from constNames import *
from map import *
############################
randomly=False
############################
def ss(s): # τυπώνει το string αφήνοντας ένα κενό στην αρχή και στο τέλος
    return f" {s.strip()} "

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
                #print("[-----------]",end='   ')
                col=BLUE
                print(col,end=' ')
                print(items,end=' ')
                print(RESET,end=' ')
            else:
                #if(ageOneDictionary[str(i+1)][0]==Taken):
                if(ageOneDictionary[str(counterOfCardsList+1)][0]==Taken):
                    col=RED
                    print(col,end=' ')
                    print(items,end=' ')
                    #print('             ',end=' ')
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

def setCardIsDiscarded(n):
    global ageOneDictionary
    ageOneDictionary[str(n+1)][0]=Discarded
    #print("mitsosss ",ageOneCards[n])
    discardedCards.append(ageOneCards[n])


def setCardIsWondered(n):
    global ageOneDictionary
    ageOneDictionary[str(n+1)][0]=CoveredByWonder


def allCardsAreTaken():
    cardsTaken=0
    for i in range(0,20):
        if ageOneDictionary[str(i+1)][0]==Taken:
            cardsTaken+=1
    #print("   Cards Taken=",cardsTaken)
    return cardsTaken==20


def giveAllTheAvailableCards():
    availableCards=[]
    for i in range(0,len(ageOneDictionary)):
        card=ageOneDictionary[str(i+1)][0]
        if card==Available:
            availableCards.append(ageOneCards[i])    
    return availableCards


def createNormalizeScoreListOfAvailableCards(prnt,availableCards):
    scoreOfAvailableCards=[]
    #availableCards=giveAllTheAvailableCards()#επιστρέφει τα ονόματα των διαθέσιμων καρτών
    for card in availableCards:
        scoreOfAvailableCards.append(evaluateTheCard(gameAgeOneCards.index(card)))#h z list exei mesa score[a,b,c]
    #print(scoreOfAvailableCards)
    HighestScore=max(scoreOfAvailableCards)
    LowestScore=min(scoreOfAvailableCards)        
    # print(YELLOW,LowestScore,HighestScore,RESET)  \  
    # print(GREEN,availableCards,RESET)
    # print(RED,scoreOfAvailableCards,RESET)
    normalizedScoreList=[]   
    for i in range(0,len(scoreOfAvailableCards)):        
        if HighestScore==LowestScore:
            normalizedScoreList.append(1)
        else:
            normalizedScoreList.append((scoreOfAvailableCards[i]-LowestScore)/(HighestScore-LowestScore))
    if prnt==1:
        print(BLUE,normalizedScoreList,RESET)
    return normalizedScoreList
    
   

def selectTheHeighestScoreCardFromAvailble2():
    while(not allCardsAreTaken()):
        availableCards=giveAllTheAvailableCards() #επιστρέφει τα ονόματα των διαθέσιμων καρτών
        indexOfMaxScoredCardInAvailableList=createNormalizeScoreListOfAvailableCards(1,availableCards).index(max(createNormalizeScoreListOfAvailableCards(0,availableCards)))    
        #print('222 ', availableCards[indexOfMaxScoredCardInAvailableList])
        return gameAgeOneCards.index(availableCards[indexOfMaxScoredCardInAvailableList])    
    return EndOfCards

def selectTheHeighestScoreCardFromAvailble():    
    availableCards=giveAllTheAvailableCards() #επιστρέφει τα ονόματα των διαθέσιμων καρτών    
    #print('999')
    indexOfMaxScoredCardInAvailableList=createNormalizeScoreListOfAvailableCards(1,availableCards).index(max(createNormalizeScoreListOfAvailableCards(0,availableCards)))    
    #print('888 ', availableCards[indexOfMaxScoredCardInAvailableList])
    return gameAgeOneCards.index(availableCards[indexOfMaxScoredCardInAvailableList])    

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



def playerDecidesActionForAgeOneCard():
    actionPDF=[70,30,0]
    #actionForFreeCard=[95,5]
    action=getRand(actionPDF)+actionOffset
    return action

def playerActs(action,card): 
    #print('card=>',card)   
    if action==BuildBuilding:
        if playerBuildsBuilding(card):
            getAgeOneCard(card)          
            #return True
        else:
            return False
    elif action==Discard:
        playerDiscardsCard(card)
        setCardIsDiscarded(card)
    else:
        playerBuildsWonder(card)
    return True

                



def inspectAgeOneCard():
    global ageOneDictionary
    numberOfCardToInspect=selectTheHeighestScoreCardFromAvailble()
    if numberOfCardToInspect==EndOfCards:
        return EndOfCards
    return numberOfCardToInspect
    

def getAgeOneCard(numberOfCardToGet):
    global ageOneDictionary
    setCardIsTaken(numberOfCardToGet)
    releaseCardBounds(numberOfCardToGet)
    print(playerName[currentPlayer[0]],' has ',ss(ageOneCards[numberOfCardToGet][1:-1]),' and decides...') 
    return numberOfCardToGet

def getAgeOneCard2():
    global ageOneDictionary
    numberOfCardToGet=selectTheHeighestScoreCardFromAvailble()
    #numberOfCardToGet=selectRandomlyAgeOneCard()

    if numberOfCardToGet==EndOfCards:
        return EndOfCards
    setCardIsTaken(numberOfCardToGet)
    releaseCardBounds(numberOfCardToGet)
    print(playerName[currentPlayer[0]],' has ',ageOneCards[numberOfCardToGet],' and decides...') 
    return numberOfCardToGet


def cityOfPlayerNames():    
    str2="\nItem      | qnt\n"
    str2+="----------+----\n"
    uniqueItems=list(set(cityOfPlayer[currentPlayer[0]]))
    for uItem in uniqueItems:
        times=cityOfPlayer[currentPlayer[0]].count(uItem)
        if uItem>100 and uItem!=Attack:
            spaces=" "*(10-len(lista[uItem]))
            str2+=lista[uItem]+ spaces+ "| "
            str2+=str(times)+"\n"
    return str2

def rearrangePlayerList(): # set to index 0 the coins that current player has spent for build building
    newList=[cityOfPlayer[currentPlayer[0]][0]]
    cns=cityOfPlayer[currentPlayer[0]][0]
    for i in range(1,len(cityOfPlayer[currentPlayer[0]])):
        if cityOfPlayer[currentPlayer[0]][i]<100:
            cns+=i
        else:
            newList.append(cityOfPlayer[currentPlayer[0]][i])
    newList[0]=cns
    return newList
def playerHasMaterialToBuildTheCard(material):
    return cityOfPlayer[currentPlayer[0]].count(material)>0

def playerHasMaterialsToBuildTheCard(card):
    for material in cardsDict["Age1"][gameAgeOneCards[card]][1][1:]:
        if not(playerHasMaterialToBuildTheCard(material)):
            return False
    return True
def playerMeetsCardRequirements(card):
    return coins[currentPlayer[0]]>=lookAtCostOfCard(card)[0] and playerHasMaterialsToBuildTheCard(card)

def timesToAttack(card):
    times=0
    for i in (cardsDict["Age1"][gameAgeOneCards[card]][2]):
            if i==Attack:
                times=times+1
    return times

def ifCardHadAttack(card):
    push=0
    if Attack in cardsDict["Age1"][gameAgeOneCards[card]][2]: 
        if currentPlayer[0]==Human:
            strategyIndicatorPosition[0]=strategyIndicatorPosition[0]+timesToAttack(card)
        else:
            strategyIndicatorPosition[0]=strategyIndicatorPosition[0]-timesToAttack(card)

def playerBuildsBuilding(card): #for card =free money,no  check if its possible
    global cityOfPlayer,coins
    if playerMeetsCardRequirements(card):
        ifCardHadAttack(card)
        cityOfPlayer[currentPlayer[0]].extend(cardsDict["Age1"][gameAgeOneCards[card]][2])  
        cityOfPlayer[currentPlayer[0]]=rearrangePlayerList()
        coins[currentPlayer[0]]-=lookAtCostOfCard(card)[0]
        print(GREEN,playerName[currentPlayer[0]],"gets",ss(ageOneCards[card][1:-1]),end='')
        print("and builds building and from now on has",coins[currentPlayer[0]],"coins and the following items" ,cityOfPlayerNames(),RESET) 
        #print(GREEN,playerName[currentPlayer[0]],"builds building and from now on has the following items" ,cityOfPlayerNames(),"in his city, and has ",coins[currentPlayer[0]],' coins',RESET) 
        return True        
    # else:
    #     #print(RED,playerName[currentPlayer[0]],"coudn't  build the building, his city remains unchanged :" ,*cityOfPlayer[currentPlayer[0]],RESET)         
    #     print(RED,playerName[currentPlayer[0]],"coudn't  build the building, his city remains unchanged :" ,cityOfPlayerNames(),RESET)         
    return False

def playerDiscardsCard(card):
    print(RED,playerName[currentPlayer[0]],"discards the Age One card:",ss(ageOneCards[card][1:-1]),RESET)
    setCardIsDiscarded(card)
    releaseCardBounds(card)

    
def playerBuildsWonder(card):
    print(YELLOW,playerName[currentPlayer[0]],"gets" + ss(ageOneCards[card][1:-1])+"and builds wonder",RESET)
    setCardIsWondered(card)
    releaseCardBounds(card)


def releaseCardBounds(card):
    global ageOneDictionary
    for i in range (0,14):
        if ageOneDictionary[str(i+1)][1]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1
            #print('444 ',gameAgeOneCards[i],ageOneDictionary[str(i+1)])
        if  ageOneDictionary[str(i+1)][2]==str(card+1):
            ageOneDictionary[str(i+1)][0]-=1
            #print('333 ',gameAgeOneCards[i],ageOneDictionary[str(i+1)])



os.system('cls')

def playAgeOneGameInit():
    shuffleAgeOneCards()
    getTwentyAgeOneCards()
    createStack()

def selectOneCard():
    selectAnotherCard=True
    tries=0        
    while(selectAnotherCard):
        numberOfCardToInspect=inspectAgeOneCard()
        if tries<100:                    
            action=playerDecidesActionForAgeOneCard()  
        else:
            action=Discard      
        selectAnotherCard=not playerActs(action,numberOfCardToInspect)  
        tries+=1

def playAgeOneGame():    
    updateAndPrintAgeOneStack()
    selectOneCard()
    switchPlayer()    
    cardsOnBoard[0]=cardsOnBoard[0]-1
    if cardsOnBoard[0]>0:
        return stateOne
    print("End of Age One Cards!")    
    #return finalState
    return stateTwoInit



    


#playAgeOneGame()
