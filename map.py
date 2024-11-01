import random

progressIndicators=["agriculture","architecture","economy","law","masonry","mathematics","philosophy","strategy","theology","urbanism"]
gameProgressIndicators=[]
isGameProgressIndicatorOnBoard=[True,True,True,True,True]

strategyIndicatorPosition=0

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
regionColors=[LIGHT_GRAY,BRIGHT_RED,BRIGHT_YELLOW,BRIGHT_GREEN,BRIGHT_MAGENTA]


def shuffleProgressIndicators():
    global progressIndicators,gameProgressIndicators
    random.shuffle(progressIndicators)
    gameProgressIndicators=progressIndicators[:5]

def printStrategyBoard():
    global strategyIndicatorPosition   
    str="[C "
    for i in range(0,19): 
        ind=i-9
        if i==9:
            ch="  "
        else:
            ch=""
        if i==strategyIndicatorPosition+9:
            str+=ch+regionColors[getReg(ind)]+"(S)"+ch+RESET
        else:
            str+=ch+regionColors[getReg(ind)]+"( )"+ch+RESET
    str+=" H]"
    print(str)

def getReg(i):
    #global strategyIndicatorPosition
    if i==0:
        reg=0
    else:
        reg=1
    return reg*abs((abs(i) // 3)+1)   

def printProgressIndicators():
    str=""
    for i in range(0,5):
        if isGameProgressIndicatorOnBoard[i]==True:
            str+=LIGHT_GRAY+gameProgressIndicators[i]+'  '+RESET
        else:
            str+=DARK_GRAY+gameProgressIndicators[i]+'  '+RESET
    print(str)

shuffleProgressIndicators()
printProgressIndicators()
printStrategyBoard()