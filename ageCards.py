from constNames import *

# initialize age 1 attributes
gameAgeOneCards=[]
gameAgeOneCardsIsTurned=[False]*20
gameAgeOneCardsStacks=[]
gameAgeOneCardsIsPicked=[False]*20


#age 1 card names
cardsDict={
    "Age1":{
    "LumberYard" :[Brown, [0], [0,Wood]],
    "LoggingCamp": [Brown, [1], [0,Wood]],
    "ClayPool": [Brown, [0], [0,Brick]],
    "ClayPit" :[Brown, [1], [0,Brick]],
    "Quarry":[Brown, [0], [0,Stone]],
    "StonePit":[Brown, [1], [0,Stone]],
    "Glassworks":[Grey, [1], [0,Glass]],
    "Press":[Grey, [1], [0,Papyrus]],
    "GuardTower":[Red, [0], [0,Attack]],
    "WorkShop":[Green, [0,Papyrus], [0,Triangle,Vpoint]],
    "Apothecary":[Green, [0,Glass], [0,Wheel,Vpoint]],
    "StoneReserve":[Gold, [3], [0,StoneDec]],
    "ClayReserve":[Gold, [3], [0,BrickDec]],
    "WoodReserve":[Gold, [3], [0,WoodDec]],
    "Stable":[Red, [0,Wood], [0,Attack,Petal]],
    "Garrison":[Red, [0,Book], [0,Attack,Knife]],
    "Palisade":[Red, [2], [0,Attack,Castle]],
    "Scriptorium":[Green, [2], [0,Feather,Book]],
    "Pharmacist":[Green, [2], [0,Plate,Setting]],
    "Theater":[Blue, [0], [0,Vpoint,Vpoint,Vpoint]],
    "Altar":[Blue, [0], [0,Vpoint,Vpoint,Vpoint]],
    "Baths":[Blue, [0,Stone], [0,Vpoint,Vpoint,Vpoint]],
    "Tavern":[Gold, [0], [4,Vase]]       
    },
    "Age2":{
        "Sawmill":[0,0,0,0,0,0,0,0,2],"Brickyard":[0,0,0,0,0,0,0,0,2],"ShelfQuarry":[0,0,0,0,0,0,0,0,2],"Glassblower":[0,0,0,0,0,0,0,0,0],"DryingRoom":[0,0,0,0,0,0,0,0,0],
        "Walls":[0,0,2,0,0,0,0,0,0],"Forum":[0,1,0,0,0,0,0,0,3],"Caravansery":[0,0,0,1,1,0,0,0,2],"CustomsHouse":[0,0,0,0,0,0,0,0,4],"Tribunal":[2,0,0,1,0,0,0,0,0],
        "HorseBreeders":[1,1,0,0,0,0,0,0,0],"Barracks":[0,0,0,0,0,0,0,0,3],"ArcheryRange":[1,0,1,0,1,0,0,0,0],"ParadeGround":[0,2,0,1,0,0,0,0,0],"Library":[1,0,1,1,0,0,0,0,0],
        "Dispensary":[0,2,1,0,0,0,0,0,0],"School":[1,0,0,0,2,0,0,0,0],"Laboratory":[1,0,0,2,0,0,0,0,0],"Statue":[0,2,0,0,0,0,0,0,0],"Temple":[1,0,0,0,1,0,0,0,0],
        "Aqueduct":[0,0,3,0,0,0,0,0,0],"Rostrum":[1,0,1,0,0,0,0,0,0],"Brewery":[0,0,0,0,0,0,0,0,0]##τα κοστοι μονο αλλα δεν περιέχει τις καρτοχημιές κοστους και αγορας
    },
    "Age3":{
        "Arsenal":[2,3,0,0,0,0,0,0,0],"Courthouse":[0,0,0,0,0,0,0,0,8],"Academy":[1,0,1,2,0,0,0,0,0],"Study":[2,0,0,1,1,0,0,0,0],"ChamberOfCommerce":[0,0,0,0,2,0,0,0,0],
        "Port":[1,0,0,1,1,0,0,0,0],"Armory":[0,0,2,1,0,0,0,0,0],"Palace":[1,1,1,2,0,0,0,0,0],"Townhall":[2,0,3,0,0,0,0,0,0],"Obelisk":[0,0,2,1,0,0,0,0,0],
        "Forifications":[0,1,2,0,1,0,0,0,0],"SiegeWorkshop":[3,0,0,1,0,0,0,0,0],"Circus":[0,2,2,0,0,0,0,0,0],"University":[0,1,1,1,0,0,0,0,0],"Observation":[0,0,1,0,2,0,0,0,0],
        "Gardens":[2,2,0,0,0,0,0,0,0],"Pantheon":[1,1,0,0,2,0,0,0,0],"Senate":[0,2,1,0,1,0,0,0,0],"Lighthouse":[0,2,0,1,0,0,0,0,0],"Arena":[1,1,1,0,0,0,0,0,0]#τα ίδια με τα απο πάνω
    }
}

ageOneCards=list(cardsDict["Age1"].keys())
ageTwoCards=list(cardsDict["Age2"].keys())
ageThreeCards=list(cardsDict["Age3"].keys())

# initial stacks
ageOneDictionary={
    "1":[3,"3","4"],
    "2":[3,"4","5"],
    "3":[3,"6","7"],
    "4":[3,"7","8"],
    "5":[3,"8","9"],
    "6":[3,"10","11"],
    "7":[3,"11","12"],
    "8":[3,"12","13"],
    "9":[3,"13","14"],
    "10":[3,"15","16"],
    "11":[3,"16","17"],
    "12":[3,"17","18"],
    "13":[3,"18","19"],
    "14":[3,"19","20"],
    "15":[1],
    "16":[1],
    "17":[1],
    "18":[1],
    "19":[1],
    "20":[1],
}
