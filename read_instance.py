import numpy as np

def readInstance(instance):
    file = open(instance, "r")
    
    lines = file.readlines()
    lines = [line.replace('\n', ' ').strip().split(" ") for line in lines]
    
    elements = []
    
    for line in lines:
        elements += line
    
    elements = list(map(int, elements))
    
    rows = elements.pop(0)
    columns = elements.pop(0)
    
    costs = [int(i) for i in elements[:columns]]
    coverageCostVector = np.array(costs)
    
    elements = elements[columns:]
    
    subsetsList = []
    coverageMatrix = np.zeros((rows, columns))
    
    for item in range(rows): 
        subsetSize = elements.pop(0)
        subSet = elements[:subsetSize]
        subSet = list(map(lambda element:element-1, subSet))
        coverageMatrix[item, subSet] = 1
        subsetsList.append(subSet)
        elements = elements[subsetSize:]
    
    setCoverginProblem = {
        "columns": columns,
        "rows": rows,
        "coverageCostVector": coverageCostVector,
        "coverageMatrix": coverageMatrix
    }
    
    return setCoverginProblem    
    