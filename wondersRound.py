import random

wonderCostDict={ #in list only costs are shown///  the code is  [wood,brick,stone,glass,papyrus]
    "TheAppianWay":[0,2,2,0,1],"CircusMaximus":[1,0,2,1,0],"TheColossus":[0,3,0,1,0],"TheGreatLibrary":[3,0,0,1,1],"TheGreatLighthouse":[1,0,1,0,2],"TheHangingGardens":[2,0,0,1,1],
    "TheMausoleum":[0,2,0,2,1],"Piraeus":[2,1,1,0,0],"ThePyramids":[0,0,3,0,1],"TheSphinx":[0,1,1,2,0],"TheStatueOfZeus":[1,1,1,0,2],"TheTempleOfArtemis":[1,0,1,1,1]
    }

wonderCards=(list(wonderCostDict.keys()))     #we take only the name of the dictionary as list.


def shuffleWonderCards(): #shuffles wonderCards and gives 2  4card-lists for the 2 rounds
    global wonderCards,gameWonderCards,roundOneWonderCards,roundTwoWonderCards
    random.shuffle(wonderCards)
    gameWonderCards=wonderCards[:8]             #ανακάτεμα WonderCards και τυχαάια επιλογή 8
    roundOneWonderCards=wonderCards[:4]
    roundTwoWonderCards=wonderCards[4:8]
