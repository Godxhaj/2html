import random

progressIndicators=["agriculture","architecture","economy","law","masonry","mathematics","philosophy","strategy","theology","urbanism"]
gameProgressIndicators=[]

def shuffleProgressIndicators():
    global progressIndicators,gameProgressIndicators
    random.shuffle(progressIndicators)
    gameProgressIndicators=progressIndicators[:5]


shuffleProgressIndicators()