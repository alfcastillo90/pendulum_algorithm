import numpy as np

def s4(initialPopulation):
    return np.divide(1, (1 + np.exp(np.divide(-1 * initialPopulation, 3))))

def elitist(bestRow, binaryPopulationMatrix, initialPopulation, s4Result):
    matrixRand = np.random.uniform(
        low=0.0, high=1.0, size=initialPopulation.shape)
    conditionMatrix = np.greater(np.zeros(s4Result.shape), matrixRand)
    bestIndividual = binaryPopulationMatrix[bestRow]

    binaryPopulationMatrix = np.zeros(binaryPopulationMatrix.shape)
    binaryPopulationMatrix = np.where(
        conditionMatrix == True, bestIndividual, 0)
    return binaryPopulationMatrix
