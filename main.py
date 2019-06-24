#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 20:47:59 2019

@author: tianqiluke

The main program for our project
"""

from environment import Maze
from model import DeepQNetwork


def run_maze():
    step = 0
    for episode in range(300):
        # initial observation
        observation = env.reset()

        while True:
            # render enviornment
            env.render()

            # RL choose action based on observation
            action = RL.choose_action(observation)

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            RL.store_transition(observation, action, reward, observation_)

            if (step > 200) and (step % 5 == 0):
                RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            step += 1

    # end of game
    print('game over')
    env.destroy()


if __name__ == "__main__":
    # maze game
    env = Maze()
    
#    RL = DeepQNetwork(env.n_actions, env.n_features,
#                      learning_rate=0.01,
#                      reward_decay=0.9,
#                      e_greedy=0.9,
#                      replace_target_iter=200,
#                      memory_size=2000
#                      )
    
    # param tuning by hand, best version for now
    RL = DeepQNetwork(env.n_actions, env.n_features,
                  learning_rate=0.005,
                  reward_decay=0.8,
                  e_greedy=0.8,
                  replace_target_iter=200,
                  memory_size=2000
                  )
    env.after(100, run_maze)
    env.mainloop()
    RL.plot_cost()
    exit()