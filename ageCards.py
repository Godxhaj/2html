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
    "Theater":[Blue, [0], [0,Vpoint,Vpoint,Vpoint,Mask]],
    "Altar":[Blue, [0], [0,Vpoint,Vpoint,Vpoint,Moon]],
    "Baths":[Blue, [0,Stone], [0,Vpoint,Vpoint,Vpoint,Drop]],
    "Tavern":[Gold, [0], [4,Vase]]       
    },
    "Age2":{
    "Sawmill": [Brown, [2], [0,Wood,Wood]],
    "Brickyard": [Brown, [2], [0,Brick,Brick]],
    "ShelfQuarry": [Brown, [2], [0,Stone,Stone]],
    "GlassBlower": [Grey, [0], [0,Glass]],
    "Drying Room": [Grey, [0], [0,Papyrus]],
    "Walls": [Red, [0,Stone,Stone],[0,Attack,Attack]],
    "Forum": [Gold, [3,Brick],[0,GlassPapyrusMix]],
    "Caravansery": [Gold, [2,Glass,Papyrus],[0,WoodStoneBrickMix]],
    "CustomsHouse": [Gold, [4],[0,GlassDec,PapyrusDec]],
    "Tribunal": [Blue, [0,Wood, Wood,Glass], [0,Vpoint,Vpoint,Vpoint,Vpoint,Vpoint]],
    "HorseBreeders": [Red, [0,Wood, Brick,Petal], [0,Attack]],
    "Barracks": [Red, [3,Knife], [0,Attack]],
    "ArcheryRange": [Red,[0,Wood,Stone,Papyrus],[0,Attack,Attack,Shield]],
    "Parade Ground": [Red, [0,Brick,Brick,Glass], [0,Attack,Attack,Helmet]],
    "Library": [Green, [0,Stone,Wood,Glass,Book], [0,Feather,Vpoint,Vpoint]],
    "Dispensary": [Green, [0,Brick,Brick,Stone,Setting],[0,Plate,Vpoint,Vpoint]],
    "School": [Green, [0,Wood,Papyrus,Papyrus],[0,Vpoint,Wheel,Harp]],
    "Laboratory": [Green, [0,Wood,Glass,Glass],[0,Vpoint,Triangle,Lamp]],
    "Statue": [Blue, [0,Brick,Brick,Mask],[0,Vpoint,Vpoint,Vpoint,Vpoint,Akropoli]],
    "Temple": [Blue, [0,Moon,Wood,Papyrus], [0,Vpoint,Vpoint,Vpoint,Vpoint,Sun]],
    "Aqueduct": [Blue,[0,Stone,Stone,Stone,Drop],[0,Vpoint,Vpoint,Vpoint,Vpoint,Vpoint]],
    "Rostrum": [Blue,[0,Stone,Wood],[0,Vpoint,Vpoint,Vpoint,Vpoint,Spiti]],
    "Brewery": [Gold,[0], [6,Barel]],
}

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
