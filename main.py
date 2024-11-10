from wondersRound import*
from const import *
from map import*
from ageOne import * 


grammes()
foo=True
#print(p(Castle),p(Red),p(Grey),p(Computer))
def playGame():    
    selectWonders()
    #selectRandomlyFirstPlayer() 
    shuffleAgeOneCardsAndCreateStacks()
    while foo:
        grammes()
        printGameBoard()
        keno()
        grammes()
        printAgeOneStack()
        selectAgeOneCard() #current player select
        print()
        print(HumanCards)
        print(ComputerCards)
        #printPlayerAgeOneCards #οι κάρτες του τρε.παίκτη μέχρι τούδε
        #currentPlayerDecidesAction()
        switchPlayer()

playGame()
#roundAgeOne()