import random
from constNames import *
import inspect

def p(var):
    current_frame = inspect.currentframe()
    try:
        frame_locals = current_frame.f_back.f_locals
        var_name = [name for name, value in frame_locals.items() if value is var][0]
        return f"{var_name}" 
        #print(f"Variable name: {var_name}")
    finally:
        del current_frame

currentPlayer=0
humanWonders=[]
computerWonders=[]
Noboby,Computer,Human,Burned=0,1,2,3
playerName=["Computer","Human"]

moneyOfHuman=7
moneyOfComputer=7

cardsDict={
    "Age1":{
    "Lumber_Yard" :[Brown, [0], [0,Wood]],
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




Lumber_Yard = ["Brown", [""], ["Wood"]]
Logging_Camp = ["Brown", ["1"], ["Wood"]]
Clay_Pool = ["Brown", [""], ["Brick"]]
Clay_Pit = ["Brown", ["1"], ["Brick"]]
Quarry = ["Brown", [""], ["Stone"]]
Stone_Pit = ["Brown", ["1"], ["Stone"]]
Glassworks = ["Grey", ["1"], ["Glass"]]
Press = ["Grey", ["1"], ["Papyrus"]]
Guard_Tower = ["Red", [""], ["Attack"]]
Workshop = ["Green", ["papyrus"], ["Triangle","Vpoint"]]
Apothecary = ["Green", ["glass"], ["Wheel","Vpoint"]]
Stone_Reserve = ["Gold", ["3"], ["StoneDec"]]
Clay_Reserve = ["Gold", ["3"], ["BrickDec"]]
Wood_Reserve = ["Gold", ["3"], ["WoodDec"]]
Stable = ["Red", ["wood"], ["Attack","petal"]]
Garrison = ["Red", ["brick"], ["Attack","knife"]]
Palisade = ["Red", ["2"], ["Attack","castle"]]
Scriptorium = ["Green", ["2"], ["Feather","book"]]
Pharmacist = ["Green", ["2"], ["plate","setting"]]
Theater = ["Blue", [""], ["Vpoint","Vpoint","Vpoint"]]
Altar = ["Blue", [""], ["Vpoint","Vpoint","Vpoint"]]
Baths = ["Blue", ["stone"], ["Vpoint","Vpoint","Vpoint"]]
Tavern = ["Gold", [""], ["4"]]

#CODE=[WOOD,BRICK,STONE,GLASS,PAPYRUS,ATTACK,SCIENCE,SYMBOL,FUNCTION,VPOINTS,GOLD]
HumanBank=[0,0,0,0,0,0,0,0,0,0,0,moneyOfHuman]
ComputerBank=[0,0,0,0,0,0,0,0,0,0,moneyOfComputer]