from wondersRound import*
from const import *
from map import*
from ageOne import * 


foo=True
#print(p(Castle),p(Red),p(Grey),p(Computer))
def playGame():    
    selectWonders()
    #selectRandomlyFirstPlayer() 
    shuffleAgeOneCardsAndCreateStacks()
    while foo:
        printGameBoard()
        selectAgeOneCard() #current player select
        #printPlayerAgeOneCards #οι κάρτες του τρε.παίκτη μέχρι τούδε
        #currentPlayerDecidesAction()
        switchPlayer()

playGame()
#roundAgeOne()