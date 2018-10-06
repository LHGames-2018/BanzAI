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
    elif(len(visiblePlayer) == 1):
        for k in range(1):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(8):
            vecteur.append(0)

    elif(len(visiblePlayer) == 2):
        for k in range(2):
            vecteur.append(visiblePlayers[k].Health)
            vecteur.append(visiblePlayers[k].Position)
            vecteur.append(visiblePlayers[k].TotalResources)
            vecteur.append(visiblePlayers[k].AttackPower)
        for n in range(4):
            vecteur.append(0)


return vecteur

    def decide_action(self, priority, gameMap, visiblePlayers):
        
        directionEnemy = Point()
        directionCollect = Point()
        posPlayer = Point(self)
        tileHaut = Point(posPlayer.x, posPlayer.y +1)
        tileDroite = Point(posPlayer.x + 1, posPlayer.y)
        tileBas = Point(posPlayer.x, posPlayer.y - 1)
        tileGauche = Point(posPlayer.x - 1, posPlayer.y)
        
        for i in range(len(visiblePlayers)-1):
            posEnemy = Point(visiblePlayers[i])
            if posPlayer.x - posEnemy.x == 1:
               directionEnemy.x = -1
            if posPlayer.x - posEnemy.x == -1:
                directionEnemy.x = 1
            if posPlayer.y - posEnemy.y == 1:
                directionEnemy.y = -1
            if posPlayer.y - posEnemy.y == -1:
                directionEnemy.y = 1

            if gameMap.getTileAt(gameMap, tileHaut) == 4:
                directionCollect.y = 1
            if gameMap.getTileAt(gameMap, tileDroite) == 4:
                directionCollect.x = 1
            if gameMap.getTileAt(gameMap, tileBas) == 4:
                directionCollect.y = -1
            if gameMap.getTileAt(gameMap, tileGauche) == 4:
                directionCollect.x = -1
                
        switcher = {
                0:create_move_action(Point(-1,0)),
                1:create_move_action(Point(1,0)),
                2:create_move_action(Point(0,1)),
                3:create_move_action(Point(0,-1)),
                4:create_attack_action(direction),
                5:create_collect_action(directoinCollect),
                6:create_purchase_action(Sword),
                7:create_upgrade_action(CollectingSpeed),
                8:create_heal_action()
                }