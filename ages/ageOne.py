import random


ageOneCards=["LumberYard","LoggingCamp","ClayPool","ClayPit","Quarry","StonePit","Glassworks","Press","GuardTower",
"WorkShop","Apothecary","StoneReserve","ClayReserve","WoodReserve","Stable","Garrison","Palisade","Scriptorium","Pharmacist",
"Theater","Altar","Baths","Tavern"]
gameAgeOneCards=[]
gameAgeOneCardsIsTurned=[False]*20
gameAgeOneCardsStacks=[]
gameAgeOneCardsIsPicked=[False]*20


def shuffleAgeOneCardsAndCreateStacks():
    global ageOneCards,gameAgeOneCards,gameAgeOneCardsStacks,gameAgeOneCardsIsTurned
    random.shuffle(ageOneCards)
    gameAgeOneCards=ageOneCards[:20]# εχω αφαιρέσει 3
    s11=gameAgeOneCards[:2]
    gameAgeOneCardsIsTurned[:2]=[True]*2
    s12=gameAgeOneCards[2:5]
    gameAgeOneCardsIsTurned[2:5]=[False]*3
    s13=gameAgeOneCards[5:9]
    gameAgeOneCardsIsTurned[5:9]=[True]*4
    s14=gameAgeOneCards[9:14]
    gameAgeOneCardsIsTurned[9:14]=[False]*5
    s15=gameAgeOneCards[14:20]
    gameAgeOneCardsIsTurned[14:20]=[True]*6
    gameAgeOneCardsStacks=[s11,s12,s13,s14,s15]

shuffleAgeOneCardsAndCreateStacks()
print(gameAgeOneCardsStacks)
print(gameAgeOneCardsIsTurned)