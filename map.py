import random
def shuffleProgressIndicators():
    global progressIndicators,gameProgressIndicators
    random.shuffle(progressIndicators)
    gameProgressIndicators=progressIndicators[:5]