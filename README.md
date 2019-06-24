# rl-final-project

Solve maze problem using Deep Q Network

# Overview

This is the final project for Reinforcement Learning course at USF. The problem we are solving is to train an agent to learn the correct route through a maze using Deep Q Network.

# Dependencies

Building the maze environment is not the core of this course, we modified the [lvidarte](https://github.com/lvidarte/maze) and [Derek Vidovic](http://new.math.uiuc.edu/math198/MA198-2012/vidovic2/python/Maze.py) scripts which were built under *Tkinter* to make the specific environment for our problem. You also need numpy, pandas, tensorflow (1.0-1.2) and Python 3.6 to run this project

# Usage

First move to the project folder:

```bash
$ cd rl-final-project
```

then run the program using the main script

```bash
$ python main.py
```

# Result

RL is always hard for training. At first, the agent was unable to learn the correct path with common hyperparameters like 0.01 learning rate, 0.9 exploration rate, we guess this wass because we were dealing with a small environment and the agent was easy to get negative feedbacks. We observed that if agent got many negative feedbacks at first few tries, it would be hard to learn the correct way in the end. Some research said too many negative feedbacks at first is not good for networking training. Then we tunned the hyperparameters for a small learning rate, higher exploration rate and we found that the agent was able to learn the correct route through the maze for 80% of the time. 

