import Player

class Agent:
    def __init__(self):
        pass

    def getRewards(prevInfo, nextInfo):
        rewards = 0
        rewards += (nextInfo.Score - prevInfo.score) / 100
        if (nextInfo.health < prevInfo.health):
            rewards -= 5
        else if (nextInfo.health > prevInfo.health):
            rewards += 5
        
