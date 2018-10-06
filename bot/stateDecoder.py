import numpy as np

def stateEncoder(gameMap, visiblePlayers):
    vecteur = []
    for i in range(len(gameMap.tiles)-1):
        vecteur.append(gameMap.tiles[i])

    for m in range(0,11,4 ):
        vecteur.append(0)
        vecteur.append(0)
        vecteur.append(0)
        vecteur.append(0)
    if(len(visiblePlayers)>2):
        for j in range(0,11,4 ):
        vecteur.append(visiblePlayers[j].Health)
        vecteur.append(visiblePlayers[j+1].Position)
        vecteur.append(visiblePlayers[j+2].TotalResources)
        vecteur.append(visiblePlayers[j+3].AttackPower)
    elif (len(visiblePlayers) == 0):

    else:
        for k in range(0,(len(visiblePlayer)*4)-1,4):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k+1].Position)
            vecteur.append(visiblePlayers[k+2].TotalResources)
            vecteur.append(visiblePlayers[k+3].AttackPower)

return vecteur
