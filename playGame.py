import constNames
from wondersRound import*
from const import *
from map import*
from ageOne import * 
from ageTwo import *
from constNames import *
import os

def playAgeTwoGame():
    print()

def playAgeThreeGame():
    print()

os.system('cls')
def playGame():        
    printGameStartLogo()
    selectFirstPlayer() #επιλέγεται τυχαία ο πρώτος παίκτης μόνο στην εκκίνηση του παιχνιδιού
    # παίξιμο της φάσης επιλογής καρτών Wonder     
    playWonder()   
    while currentState[0]!=finalState:
        # κύρια φάση παιχνιδιού
        #printGameBoard()        
        if currentState[0]==stateOneInit:
            playAgeOneGameInit()            
            nextState=stateOne
        elif currentState[0]==stateOne:    
            nextState=playAgeOneGame()
            printGameBoard()
        elif currentState[0]==stateTwoInit:
            playAgeTwoGameInit()
            nextState=stateTwo
        elif currentState[0]==stateTwo:                        
            nextState=playAgeTwoGame()
            printGameBoard()
        # elif currentState[0]==stateThree:
        #     nextState=playAgeThreeGame()
        currentState[0]=nextState

playGame()
print( cardsDict["Age1"]["[  ClayPool  ]"][2])



#printGameStartLogo()
#selectFirstPlayer() #επιλέγεται τυχαία ο πρώτος παίκτης
#playWonder()   # παίξιμο της φάσης επιλογής καρτών Wonder 
#printGameBoard()


