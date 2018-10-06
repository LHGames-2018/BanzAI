import numpy as np
from helper import *

def stateDecoder(playerInfo, gameMap, visiblePlayers):
    vecteur = []
    vecteur.append(playerInfo.Position.x)
    vecteur.append(playerInfo.Position.y)
    for i in range(len(gameMap.tiles)-1):
        for j in range(len(gameMap.tiles[i]) - 1):
            vecteur.append(gameMap.tiles[i][j].TileContent.value)

    if(len(visiblePlayers) > 2):
        for j in range(3):
            vecteur.append(visiblePlayers[j].Health)
            vecteur.append(visiblePlayers[j].Position.x)
            vecteur.append(visiblePlayers[j].Position.y)
            vecteur.append(visiblePlayers[j].TotalResources)
            vecteur.append(visiblePlayers[j].AttackPower)
    elif (len(visiblePlayers) == 0):
        for l in range(15):
            vecteur.append(0)
    elif(len(visiblePlayers) == 1):
        for k in range(1):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position.x)
            vecteur.append(visiblePlayers[k].Position.y)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(10):
            vecteur.append(0)

    elif(len(visiblePlayers) == 2):
        for k in range(2):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position.x)
            vecteur.append(visiblePlayers[k].Position.y)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(5):
            vecteur.append(0)
    return vecteur

def decide_action(priority, gameMap, visiblePlayers, playerInfo):
        directionEnemy = Point()
        directionCollect = Point()
        posPlayer = playerInfo.Position
        tileHaut = Point(posPlayer.x, posPlayer.y - 1)
        tileDroite = Point(posPlayer.x + 1, posPlayer.y)
        tileBas = Point(posPlayer.x, posPlayer.y + 1)
        tileGauche = Point(posPlayer.x - 1, posPlayer.y)
        canAttack = False

        for i in range(len(visiblePlayers)-1):
            posEnemy = Point(visiblePlayers[i].Position.x, visiblePlayers[i].Position.y)
            if posPlayer.x - posEnemy.x == 1:
                directionEnemy.x = -1
                canAttack = True
            elif posPlayer.x - posEnemy.x == -1:
                directionEnemy.x = 1
                canAttack = True
            elif posPlayer.y - posEnemy.y == 1:
                directionEnemy.y = -1
                canAttack = True
            elif posPlayer.y - posEnemy.y == -1:
                directionEnemy.y = 1
                canAttack = True

        attackWall = False
        wallDir = Point()
        if (gameMap.getTileAt(tileHaut) == 1):
            attackWall = True
            wallDir.y = -1
        elif (gameMap.getTileAt(tileBas) == 1):
            attackWall = True
            wallDir.y = 1
        elif (gameMap.getTileAt(tileGauche) == 1):
            attackWall = True
            wallDir.x = -1
        elif (gameMap.getTileAt(tileDroite) == 1):
            attackWall = True
            wallDir.x = 1

        canCollect = False
        if gameMap.getTileAt(tileHaut) == 4:
            directionCollect.y = -1
            canCollect = True
        elif gameMap.getTileAt(tileDroite) == 4:
            directionCollect.x = 1
            canCollect = True
        elif gameMap.getTileAt(tileBas) == 4:
            directionCollect.y = 1
            canCollect = True
        elif gameMap.getTileAt(tileGauche) == 4:
            directionCollect.x = -1
            canCollect = True


        if priority == 0:
            return create_move_action(Point(-1,0))
        elif priority == 1:
            return create_move_action(Point(1,0))
        elif priority == 2:
            return create_move_action(Point(0,1))
        elif priority == 3:
            return create_move_action(Point(0,-1))
        elif priority == 4:
            if (canAttack):
                return create_attack_action(directionEnemy)
            elif (attackWall):
                print("WALL BREAKER --------------------------")
                return create_empty_action(wallDir)
            else:
                return create_empty_action()
        elif priority == 5:
            if (canCollect):
                print("Collection --------------------------")
                return create_collect_action(directionCollect)
            else:
                return create_empty_action()
