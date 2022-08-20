import numpy as np
import time
from dotenv import load_dotenv
import os
from fitness import fitness
import read_instance as Instance
import check_solution as CheckSolution
import repair as Repair
import pendulum_algorithm as PendulumAlgorithm
import transfer_functions as TransferFunctions

load_dotenv()

scpDirectory = os.getenv('SCP_DIR')
resultsDir = os.getenv('RESULTS_DIR')
startedDate = time.time()

challenge = resultsDir.split("/")[1].split(".")[0]
result = open(resultsDir+"PSA_"+challenge+".txt", "w")

# Leemos la instancia
setCoveringProblem = Instance.readInstance(scpDirectory)
coverageMatrix = setCoveringProblem['coverageMatrix']
coverageCostVector = setCoveringProblem['coverageCostVector']
dimensions = len(coverageCostVector)
populationSize = 40
maximunIterations = 100
dictionary = {}
binarizationMethods = ['S4', 'Elitist']

dictionary['costs'] = coverageCostVector
dictionary["coverage"] = coverageMatrix
dictionary["binarizationMethods"] = binarizationMethods

initialPopulation = np.random.uniform(
    low=-10.0, high=10.0, size=(populationSize, dimensions))

binaryPopulationMatrix = np.random.randint(
    low=0, high=2, size=(populationSize, dimensions))

fitnessVector = np.zeros(populationSize)
solutionsRanking = np.zeros(populationSize)

# calculo de factibilidad de cada individuo y calculo del fitness inicial
for position in range(initialPopulation.__len__()):
    flag, aux = CheckSolution.verify(
        setCoveringProblem, binaryPopulationMatrix[position])
    if not flag:  # solucion infactible
        # matrixBin[i] = rep.reparaSimple(SCP, matrixBin[i])
        binaryPopulationMatrix[position] = Repair.complex(
            setCoveringProblem, binaryPopulationMatrix[position])

    fitnessVector[position] = fitness.fitness(
        setCoveringProblem, binaryPopulationMatrix[position])

solutionsRanking = np.argsort(fitness)  # rankings de los mejores fitnes
bestRowAux = solutionsRanking[0]

# comienzo de la metaheuristica
for iteration in range(0, maximunIterations):

    processTime = time.process_time()
    timerStart = time.time()

    best = initialPopulation[bestRowAux]
    bestBinary = binaryPopulationMatrix[bestRowAux]
    bestFitness = np.min(fitness)
    initialPopulation = PendulumAlgorithm.iterate_with_pendulum(
        initialPopulation, best, dimensions, iteration, maximunIterations)

    # Transferencia y binarizacion
    for i in range(initialPopulation.__len__()):
        s4Result = TransferFunctions.s4(initialPopulation)
        bestRow = np.argmin(solutionsRanking)
        binaryPopulationMatrix = TransferFunctions.elitist(
            bestRow, binaryPopulationMatrix, initialPopulation, s4Result)
        flag, aux = CheckSolution.verify(
            setCoveringProblem, binaryPopulationMatrix[i])
        fitnessVector[i] = fitness.fitness(
            setCoveringProblem, binaryPopulationMatrix[i])
    solutionsRanking = np.argsort(fitnessVector)

    if fitnessVector[bestRowAux] > bestFitness:
        fitnessVector[bestRowAux] = bestFitness
        binaryPopulationMatrix[bestRowAux] = bestBinary
    bestFitness = np.min(fitness)

    timerFinal = time.time()
    # calculo mi tiempo para la iteracion t
    timeEjecuted = timerFinal - timerStart
    print("iteracion: "+str(iter)+", best fitness: " +
          str(bestFitness)+", tiempo iteracion (s): "+str(timeEjecuted))
    result.write("iteracion: "+str(iter)+", best fitness: " +
                    str(bestFitness)+", tiempo iteracion (s): "+str(timeEjecuted)+"\n")

print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Best fitness: "+str(bestFitness))
result.write("Best fitness: "+str(bestFitness)+"\n")
print("Cantidad de columnas seleccionadas: "+str(sum(bestBinary)))
result.write("Cantidad de columnas seleccionadas: " +
                str(sum(bestFitness))+"\n")
print("Best solucion: \n"+str(bestFitness.tolist()))
result.write("Best solucion: \n"+str(bestFitness.tolist())+"\n")
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
tiempoFinal = time.time()
tiempoEjecucion = tiempoFinal - tiempoInicial
print("Tiempo de ejecucion (s): "+str(tiempoEjecucion))
result.write("Tiempo de ejecucion (s): "+str(tiempoEjecucion))
result.close()
print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
