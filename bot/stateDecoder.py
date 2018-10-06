import numpy as np

class stateDecoder:

def stateDecoder(gameMap, visiblePlayers):
    np vecteur = []
    for i in range(len(gameMap.tiles)-1):
        vecteur.append(gameMape.tiles[i])

    for j in range(len(visiblePlayers)-1):
        vecteur.append(visiblePlayers[j])

    return vecteur
