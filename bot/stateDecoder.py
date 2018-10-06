import numpy as np

def stateDecoder(gameMap, visiblePlayers):
    vecteur = []
    for i in range(len(gameMap.tiles)-1):
        vecteur.append(gameMap.tiles[i])


    if(len(visiblePlayers)>2):
        for j in range(3):
            vecteur.append(visiblePlayers[j].Health)
            vecteur.append(visiblePlayers[j].Position)
            vecteur.append(visiblePlayers[j].TotalResources)
            vecteur.append(visiblePlayers[j].AttackPower)
    elif (len(visiblePlayers) == 0):
        for l in range(12):
            vecteur.append(0)
    elif((len(visiblePlayer) == 1 ):
        for k in range(1):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(8):
            vecteur.append(0)

    elif((len(visiblePlayer) == 1 ):
        for k in range(2):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(4):
            vecteur.append(0)


return vecteur
