from helper import *
from bot.agent import *

class Bot:
    def __init__(self):
        self.initialize = True
        self.agent = Agent()
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        if (self.initialize):
            self.agent.setPrevInfo(playerInfo)
            self.initialize = False
        self.agent.setNextInfo(playerInfo)
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """
        # action = self.agent.action(gameMap, visiblePlayers)
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        return create_move_action(-1, 0)

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass
    def getState():
        return self.state
