from helper.player import *
from bot.stateDecoder import *
from bot.bot import *
import numpy as np
import random
import tensorflow as tf
import os
os.environ['KERAS_BACKEND'] = 'theano'
import keras
from keras.layers import Dense, Flatten, Dropout, Activation
from keras.optimizers import Adam
from collections import deque
import gym

class Agent:
    def __init__(self):
        self.prevInfo = None
        self.nextInfo = None
        self.state = np.reshape(np.zeros(417), [1, 417])
        self.n_actions = 6
        self.n_states = 417
        self.epsilon = 1.0
        self.episodes = 1000
        self.e_decay = 0.9999
        self.epsilon_min = 0.01
        self.discount_factor = 0.95
        self.memory = deque(maxlen=2000)

        self.model = keras.Sequential()
        self.model.add(Dense(32, input_shape = (self.n_states,), activation="relu"))
        self.model.add(Dense(64, activation = "relu"))
        self.model.add(Dense(64, activation = "relu"))
        self.model.add(Dense(self.n_actions, activation="linear"))
        self.model.compile(loss='mse', optimizer=Adam(lr=0.001))

    def setNextInfo(self, info):
        self.nextInfo = info

    def setPrevInfo(self, info):
        self.prevInfo = info

    def get_samples(self, size = 32):
        samples = random.sample(self.memory, size)
        return samples

    def update_Qs(self):
        samples = self.get_samples()
        for next_state, action, reward, state, done_sample in samples:
            Q_target = self.model.predict(state)[0]
            Q_target[action] = reward
            if(not done_sample):
                Q_target[action] += self.discount_factor*np.amax(self.model.predict(next_state)[0])
            self.model.fit( state, np.array([Q_target]),epochs = 1, verbose = 0)

    def hasDied(self):
        return (self.prevInfo.Health == 0)

    def getRewards(self, action, gameMap):
        rewards = 0
        next = self.nextInfo
        prev = self.prevInfo

        #If he got more resources
        if (next.CarriedResources > prev.CarriedResources):
            rewards += 10

        #If he lost HP
        if (next.Health < prev.Health):
            rewards -= 5
        #If he gained HP
        elif (next.Health > prev.Health):
            rewards += 5

        if (len(next.CarriedItems) > len(prev.CarriedItems)):
            rewards += 5

        #If his capacities were improved
        if (next.CarryingCapacity > prev.CarryingCapacity):
            rewards += 10

        if (next.AttackPower > prev.AttackPower):
            rewards += 10

        if (next.Defence > prev.Defence):
            rewards += 10

        if (next.MaxHealth > prev.MaxHealth):
            rewards += 10

        if (next.CollectingSpeed > prev.CollectingSpeed):
            rewards += 10

        if (action == 5):
            posPlayer = next.Position
            tileHaut = Point(posPlayer.x, posPlayer.y - 1)
            tileDroite = Point(posPlayer.x + 1, posPlayer.y)
            tileBas = Point(posPlayer.x, posPlayer.y + 1)
            tileGauche = Point(posPlayer.x - 1, posPlayer.y)
            if (gameMap.getTileAt(tileHaut) == 4
                or gameMap.getTileAt(tileDroite) == 4
                or gameMap.getTileAt(tileBas) == 4
                or gameMap.getTileAt(tileGauche) == 4):
                print("----- +50 --------")
                rewards += 50

        #Add reward depending on the augmentation of score
        rewards += (next.Score - prev.Score) / 100

        #If he's dead
        if (next.Health == 0):
            rewards = -100

        if (rewards == 0):
            rewards = -1
        self.prevInfo = self.nextInfo
        return rewards


    def action(self, gameMap, visiblePlayers):
        next_state = stateDecoder(self.nextInfo, gameMap, visiblePlayers)
        if (self.epsilon >= random.random()):
            action = random.randint(0, 5)
        else:
            action = np.argmax(self.model.predict(self.state)[0])
        if(self.epsilon > self.epsilon_min):
            self.epsilon *= self.e_decay

        reward = self.getRewards(action, gameMap)
        if (reward > 0):
            print("Reward : ", reward, "---------------------")
        next_state = np.reshape(next_state, [1, self.n_states])
        done = self.hasDied()
        self.memory.append([next_state, action, reward, self.state, done])

        if len(self.memory) > 32:
            self.update_Qs()

        self.state = next_state
        return decide_action(action, gameMap, visiblePlayers, self.prevInfo)
