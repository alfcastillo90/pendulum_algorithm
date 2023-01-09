import math 
import numpy as np
import random

def calculate_pend(iteration, maximumIteration, rand):
  pend = math.exp((-1)*(iteration/maximumIteration)*math.cos(math.pi*rand))
  return pend

def agent_position(bestPosition, previousPosition, pend):
  position = previousPosition + pend * (bestPosition - previousPosition)
  return position

def iterate_with_pendulum(agents, bestPosition, dimensions, iteration, maximumIterations):
    for i in range(agents.__len__()):
        for j in range(dimensions):
          rand = random.uniform(0.0, 1.0)
          pend = calculate_pend(iteration, maximumIterations, rand)
          agents[i][j] = agent_position(bestPosition[j], agents[i][j-1], pend)
    return np.array(agents)
            
        