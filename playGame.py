import constNames
from wondersRound import*
from const import *
from map import*
from ageOne import * 
from ageTwo import *
from constNames import *
from cVictory import *
import os
import sys
toFile=11
def playAgeTwoGame():
    print()

def playAgeThreeGame():
    print()

os.system('cls')
def playGame():   
    f = open('output.txt','w')
    if toFile==1:
        sys.stdout = f         
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
            nextState=playTwo()
            printGameBoard()
        # elif currentState[0]==stateThree:
        #     nextState=playAgeThreeGame()
        currentState[0]=nextState

playGame()
printFinalVictoryPoints()



#printGameStartLogo()
#selectFirstPlayer() #επιλέγεται τυχαία ο πρώτος παίκτης
#playWonder()   # παίξιμο της φάσης επιλογής καρτών Wonder 
#printGameBoard()
class CaptureOutput:
    def __init__(self, filename):
        self.terminal = sys.stdout  # Store original stdout
        self.log = open(filename, "w", encoding="utf-8")

    def write(self, message):
        self.terminal.write(message)  # Print to terminal
        self.log.write(message)  # Save to file

    def flush(self):
        self.terminal.flush()
        self.log.flush()

# Redirect output to both terminal and file
sys.stdout = CaptureOutput("output.txt")

# Example prints with colors
print("\033[31mRed Text\033[0m and \033[32mGreen Text\033[0m")

# Restore original stdout after execution
sys.stdout = sys.__stdout__

print("Output saved to output.txt")

