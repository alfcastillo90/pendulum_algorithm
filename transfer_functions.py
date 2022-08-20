import numpy as np


def s4(populationMatix):
    return np.divide(1, (1 + np.exp(np.divide(-1 * populationMatix, 3))))


def elitist(binaryPopulationMatrix, populationMatix, solutionsRanking):
    matrixRand = np.random.uniform(
        low=0.0, high=1.0, size=populationMatix.shape)
    conditionMatrix = np.greater(np.zeros(populationMatix.shape), matrixRand)
    bestIndividual = binaryPopulationMatrix[np.argmin(solutionsRanking)]

    binaryPopulationMatrix = np.zeros(binaryPopulationMatrix.shape)
    binaryPopulationMatrix = np.where(
        conditionMatrix == True, bestIndividual, 0)
    return binaryPopulationMatrix
