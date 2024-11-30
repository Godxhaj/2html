import constNames
from wondersRound import*
from const import *
from map import*
from ageOne import * 
from constNames import *
import os


os.system('cls')
def playGame():    
    foo=True
    printGameStartLogo()
    selectFirstPlayer() #επιλέγεται τυχαία ο πρώτος παίκτης
    playWonder()   # παίξιμο της φάσης επιλογής καρτών Wonder 
    while foo:        
        printGameBoard()        
        playAgeOne()
        # selectAgeOneCard() #current player select
        # print()
        # print(HumanCards)
        # print(ComputerCards)
        # #printPlayerAgeOneCards #οι κάρτες του τρε.παίκτη μέχρι τούδε
        # #currentPlayerDecidesAction()
        switchPlayer()
        foo=False

playGame()


