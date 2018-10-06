import Player
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
        self.n_states = 2
        self.neural_net(input_dim = n_states, output_dim = n_actions)
        self.epsilon = 1.0
        self.episodes = 1000
        self.e_decay = 0.9995
        self.epsilon_min = 0.01
        self.discount_factor = 0.95
        self.memory = deque(maxlen=2000)
        self.model = keras.Sequential()
        neural_net()

    def get_samples(size = 32):
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
    
    def neural_net(input_dim, output_dim):
        self.model.add(Dense(64, input_shape = (input_dim,), activation="relu"))
        self.model.add(Dense(64, activation = "relu"))
        self.model.add(Dense(128, activation = "relu"))
        self.model.add(Dense(128, activation = "relu"))

        self.model.add(Dense(output_dim,activation="linear"))
        self.model.compile(loss='mse', optimizer=Adam(lr=0.001))    
  
    
    def action(gameMap, visiblePlayer):
        next_state = stateEncoder(gameMap, VisiblePlayer)
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
    
   
    
    def getRewards():
        nextInfo = Bot.playerInfo
        
        rewards = 0
        rewards += (nextInfo.Score - prevInfo.score) / 100
        if (nextInfo.health < prevInfo.health):
            rewards -= 5
        else if (nextInfo.health > prevInfo.health):
            rewards += 5
            
        self.prevInfo = nextInfo

