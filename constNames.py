from colors import *
currentPlayer=[0]
playerWonders=[[],[]]
Noboby,Computer,Human,Burned=-1,0,1,2
playerName=["Computer","Human"]
coins=[7,7] # coins of Computer,Human
roundOne,roundTwo=0,1

cityOfPlayer=[[],[]]
minmax=[]
playersCards=[[],[]]


lista=[-1]*100
Wood, Brick, Stone, Glass, Papyrus = 10, 11, 12, 13, 14
Attack, Vpoint = 20, 21
Feather, Triangle, Wheel, Plate = 30, 31, 32, 33
Petal, Knife, Castle, Book, Setting, Vase = 40, 41, 42, 43, 44, 45
StoneDec, BrickDec, WoodDec = 50, 51, 52
Brown, Grey, Red, Green, Gold, Blue = 61, 62, 63, 64, 65, 66

lista[Noboby] = "Noboby"
lista[Computer] = "Computer"
lista[Human] = "Human"
lista[Burned] = "Burned"

lista[Brown] = "Brown"
lista[Grey] = "Grey"
lista[Red] = "Red"
lista[Green] = "Green"
lista[Gold] = "Gold"
lista[Blue] = "Blue"

lista[Wood] = "Wood"
lista[Brick] = "Brick"
lista[Stone] = "Stone"
lista[Glass] = "Glass"
lista[Papyrus] = "Papyrus"

lista[Attack] = "Attack"
lista[Vpoint] = "Vpoint"

lista[Feather] = "Feather"
lista[Triangle] = "Triangle"
lista[Wheel] = "Wheel"
lista[Plate] = "Plate"

lista[Petal] = "Petal"
lista[Knife] = "Knife"
lista[Castle] = "Castle"
lista[Book] = "Book"
lista[Setting] = "Setting"
lista[Vase] = "Vase"

lista[StoneDec] = "StoneDec"
lista[BrickDec] = "BrickDec"
lista[WoodDec] = "WoodDec"
