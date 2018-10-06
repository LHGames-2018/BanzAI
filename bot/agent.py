import Player
import stateDecoder
import Bot
import numpy as np
import random
import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.layers import Dense, Flatten, Dropout, Activation
from tensorflow.keras.optimizers import Adam
from collections import deque
import gym

class Agent:
    def __init__(self):
        self.prevInfo = Bot.playerInfo
        self.state = []
        self.n_actions = 7
        self.n_states = 412
        self.neural_net(input_dim = n_states, output_dim = n_actions)
        self.epsilon = 1.0
        self.episodes = 1000
        self.e_decay = 0.9995
        self.epsilon_min = 0.01
        self.discount_factor = 0.95
        self.memory = deque(maxlen=2000)
        self.model = keras.Sequential()
        neural_net()

    def __get_samples(size = 32):
        samples = random.sample(memory,size)
        return samples

    def __update_Qs():
        samples = get_samples()
        for next_state, action, reward, state, done_sample in samples:
            Q_target = model.predict(state)[0]
            Q_target[action] = reward
            if(not done_sample):
                Q_target[action] += discount_factor*np.amax(model.predict(next_state)[0])
            model.fit( state, np.array([Q_target]),epochs = 1, verbose = 0)

    def __neural_net(input_dim, output_dim):
        self.model.add(Dense(64, input_shape = (input_dim,), activation="relu"))
        self.model.add(Dense(64, activation = "relu"))
        self.model.add(Dense(128, activation = "relu"))
        self.model.add(Dense(128, activation = "relu"))

        self.model.add(Dense(output_dim,activation="linear"))
        self.model.compile(loss='mse', optimizer=Adam(lr=0.001))


    def action(gameMap, visiblePlayer):
        next_state = stateDecoder(gameMap, VisiblePlayer)
        if(epsilon >= random.random()):
            action = env.action_space.sample()
        else:
            action = np.argmax(model.predict(state)[0])

        if(epsilon > epsilon_min):
            epsilon *= e_decay

        reward = getRewards()
        next_state = np.reshape(next_state, [1,n_states])
        total_reward += reward

        self.memory.append([next_state, action, reward, state, done])

        if len(memory) < 32:
            continue

        update_Qs()
        self.state = next_state

    def __getRewards():
        nextInfo = Bot.PlayerInfo
        rewards = 0

        #If he got more resources
        if (next.CarriedResources > prev.CarriedResources):
            rewards += 10

        #If he lost HP
        if (next.Health < prev.Health):
            reward -= 5
        #If he gained HP
        else if (next.Health > prev.Health):
            reward += 5

        if (len(next.CarriedItems) > len(prev.CarriedItems)):
            reward += 5

        #If his capacities were improved
        if (next.CarryingCapacity > prev.CarryingCapacity):
            reward += 10

        if (next.AttackPower > prev.AttackPower):
            reward += 10

        if (next.Defence > prev.Defence):
            reward += 10

        if (next.MaximumHealth > prev.MaximumHealth):
            reward += 10

        if (next.CollectingSpeed > prev.CollectingSpeed):
            reward += 10

        #Add reward depending on the augmentation of score
        reward += (next.Score - prev.Score) / 100

        #If he's dead
        if (next.Health == 0)
            reward = -100

        self.prevInfo = nextInfo
        return rewards
