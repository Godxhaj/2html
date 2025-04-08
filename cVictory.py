from constNames import *


def determineVictoryPoints():
    scoreOfPlayer[Computer]=cityOfPlayer[Computer].count(Vpoint)
    scoreOfPlayer[Human]=cityOfPlayer[Human].count(Vpoint)

# def getVictoryPointsFromMap():
    # print('stra =',strategyIndicatorPosition[0])    

def printFinalVictoryPoints():
    determineVictoryPoints()
    print(' Total Victory Points')
    print('  Computer : ',scoreOfPlayer[Computer])
    print('  Human    : ',scoreOfPlayer[Human])
   # getVictoryPointsFromMap()