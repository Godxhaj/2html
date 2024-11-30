from colors import *
currentPlayer=[0]
playerWonders=[[],[]]
Noboby,Computer,Human,Burned=-1,0,1,2
playerName=["Computer","Human"]
coins=[7,7] # coins of Computer,Human
roundOne,roundTwo=0,1

Turned,Taken=1,0
NoBounds=1
EndOfCards=-1

cityOfPlayer=[[],[]]
minmax=[]
playersCards=[[],[]]
discardedCards=[]

lista=[-1]*100
Wood, Brick, Stone, Glass, Papyrus = 10, 11, 12, 13, 14
GlassOrPapyrus, WoodOrStoneOrBrick=15,16
Attack, Vpoint = 20, 21
Feather, Triangle, Wheel, Plate = 30, 31, 32, 33
Petal, Knife, Castle, Book, Setting, Vase,Mask, Moon, Drop = 40, 41, 42, 43, 44, 45,46,47,48
StoneDec, BrickDec, WoodDec, GlassDec,PapyrusDec = 50, 51, 52,53,54
Brown, Grey, Red, Green, Gold, Blue = 61, 62, 63, 64, 65, 66
Shield, Helmet, Harp, Lamp, Acropoli,Sun,Home,Barel=70,71,72,73,74,75,76,77

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
lista[GlassOrPapyrus]= "GlassOrPapyrus"
lista[WoodOrStoneOrBrick]="WoodOrStoneOrBrick"

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
lista[Mask] = "Mask"
lista[Moon] = "Moon"
lista[Drop] = "Drop"


lista[StoneDec] = "StoneDec"
lista[BrickDec] = "BrickDec"
lista[WoodDec] = "WoodDec"
lista[GlassDec]="GlassDec"
lista[PapyrusDec]="PapyrusDec"

lista[Shield]="Shield"
lista[Helmet]="Helmet"
lista[Harp]="Harp"
lista[Lamp]="Lamp"
lista[Acropoli]="Acropoli"
lista[Sun]="Sun"
lista[Home]="Home"
lista[Barel]="Barel"