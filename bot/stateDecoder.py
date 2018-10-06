import numpy as np

class stateDecoder:

def stateDecoder(gameMap, visiblePlayers):
    vecteur = []
    for i in range(len(gameMap.tiles)-1):
        vecteur.append(gameMap.tiles[i])

    for j in range(len(visiblePlayers)-1):
        vecteur.append(visiblePlayers[j])

    return vecteur
