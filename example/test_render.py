import gym
import gym_bullet

import numpy as np


env = gym.make("Walker2DBulletPositionControlEnv-v0")
env.render(mode="human")

a = np.zeros(len(env.action_space.high))

o = env.reset()

while True:
    # a = env.sample_actions()
    still_open = env.render("human")
    if still_open == False:
        break
    env.step(a)
    