import random

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
wonderCostDict={ #in list only costs are shown///  the code is  [wood,brick,stone,glass,papyrus]
    "TheAppianWay":[0,2,2,0,1],"CircusMaximus":[1,0,2,1,0],"TheColossus":[0,3,0,1,0],"TheGreatLibrary":[3,0,0,1,1],"TheGreatLighthouse":[1,0,1,0,2],"TheHangingGardens":[2,0,0,1,1],
    "TheMausoleum":[0,2,0,2,1],"Piraeus":[2,1,1,0,0],"ThePyramids":[0,0,3,0,1],"TheSphinx":[0,1,1,2,0],"TheStatueOfZeus":[1,1,1,0,2],"TheTempleOfArtemis":[1,0,1,1,1]
    }

wonderCards=(list(wonderCostDict.keys()))     #we take only the name of the dictionary as list.

roundOneWonderCardsPicked=[False]*4
roundTwoWonderCardsPicked=[False]*4

def shuffleWonderCards(): #shuffles wonderCards and gives 2  4card-lists for the 2 rounds
    global wonderCards,gameWonderCards,roundOneWonderCards,roundTwoWonderCards
    random.shuffle(wonderCards)
    gameWonderCards=wonderCards[:8]             
    roundOneWonderCards=wonderCards[:4]
    roundTwoWonderCards=wonderCards[4:8]


def printRoundOneWonderCardsNames():
    str=""
    for i in range(0,4):
        lista=printValuesOfDicRoundOne(i)
        if roundOneWonderCardsPicked[i]==False:
            str+=RED +roundOneWonderCards[i]+' '+RESET
            str+=lista
        else:
            str+=CYAN+roundOneWonderCards[i]+'  '+RESET
            str+=lista
    print(str)  


def printRoundTwoWonderCardsNames():
    str=""
    for i in range(0,4):
        lista=printValuesOfDicRoundTwo(i)
        if roundTwoWonderCardsPicked[i]==False:
            str+=RED +roundTwoWonderCards[i]+' '+RESET
            str+=lista
        else:
            str+=CYAN+roundTwoWonderCards[i]+'  '+RESET
            str+=lista
    print(str)




def printValuesOfDicRoundTwo(i):#kolpo gia na ginei lista "string"
    stri=list(wonderCostDict[roundTwoWonderCards[i]])
    return str(stri)

def printValuesOfDicRoundOne(i):#kolpo gia na ginei lista "string"
    stri=list(wonderCostDict[roundOneWonderCards[i]])
    return str(stri)

shuffleWonderCards()
printRoundOneWonderCardsNames()
printRoundTwoWonderCardsNames()