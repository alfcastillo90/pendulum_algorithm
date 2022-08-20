import numpy as np
import time
from dotenv import load_dotenv
import os
from fitness import fitness
import read_instance as Instance
import check_solution as coverageMatrix
import repair as Repair

load_dotenv()

scpDirectory = os.getenv('SCP_DIR')
resultsDir = os.getenv('RESULTS_DIR')
startedDate = time.time()

# Leemos la instancia
setCoveringProblem = Instance.readInstance(scpDirectory)
coverageMatrix = setCoveringProblem['coverageMatrix']
coverageCostVector = setCoveringProblem['coverageCostVector']
dimensions = len(coverageCostVector)
populationSize = 40
maximunIterations = 100
dictionary = {}
binarizationMethods = ['S4','Elitist']

dictionary['costs'] = coverageCostVector
dictionary["coverage"] = coverageMatrix
dictionary["binarizationMethods"] = binarizationMethods
dictionary["repairType"] = 1

initialPopulation = np.random.uniform(low=-10.0, high=10.0, size=(populationSize,dimensions))

binaryPopulationMatrix = np.random.randint(low=0, high=2, size = (populationSize,dimensions))

fitnessVector = np.zeros(populationSize)
solutionsRanking = np.zeros(populationSize)

# calculo de factibilidad de cada individuo y calculo del fitness inicial
for position in range(initialPopulation.__len__()):
    flag, aux = coverageMatrix.verify(setCoveringProblem,binaryPopulationMatrix[position])
    if not flag: #solucion infactible
        # matrixBin[i] = rep.reparaSimple(SCP, matrixBin[i])
        binaryPopulationMatrix[position] = Repair.complex(setCoveringProblem, binaryPopulationMatrix[position])
        

    fitnessVector[position] = fitness.fitness(setCoveringProblem, binaryPopulationMatrix[position])

solutionsRanking = np.argsort(fitness) # rankings de los mejores fitnes
bestRowAux = solutionsRanking[0]

