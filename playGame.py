import constNames
from wondersRound import*
from const import *
from map import*
from ageOne import * 
from constNames import *
import os

foo=True
os.system('cls')
def playGame():    
    printGameStartLogo()
    selectFirstPlayer() #επιλέγεται τυχαία ο πρώτος παίκτης
    playWonder()   # παίξιμο της φάσης επιλογής καρτών Wonder 
    shuffleAgeOneCardsAndCreateStacks()    
    while foo:        
        printGameBoard()        
        # grammes()
        printAgeOneStack()
        selectAgeOneCard() #current player select
        print()
        print(HumanCards)
        print(ComputerCards)
        #printPlayerAgeOneCards #οι κάρτες του τρε.παίκτη μέχρι τούδε
        #currentPlayerDecidesAction()
        switchPlayer()

playGame()


