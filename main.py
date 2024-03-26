import numpy as np
import random as rd
from random import *
from genetic_alg import *


if __name__ == "__main__":

    itemID = np.append([1,2,3,4,5,6,7,8,9,10,11],[12])
    itemWeights = np.append([20, 30, 60, 90, 50, 70, 30, 30, 70, 20, 20], [60])
    itemVals = np.append([6,5,8,7,6,9,4,5,4,9,2], [1])

    #represents size of initial population
    num_chromosomes = 16
    populationDimensions = (num_chromosomes, itemID.shape[0])

    # random population represented as an array of arrays (each sub array is a 
    # chromosome that represents an individual)
    initialPopulation = np.random.randint(2, size = populationDimensions)

    numGenerations = 70
    maxWeight = 250

    #represents which items to bring
    best_chromosome = genetic_algorithm(initialPopulation, itemWeights, 
                                            itemVals, numGenerations, 250)

    backpackItems = itemID * best_chromosome
    final_items = []
    for i in range(backpackItems.shape[1]):
        if backpackItems[0][i] != 0:
            final_items.append(backpackItems[0][i])
    print("Bringing items:")
    print(final_items)
    optimal = np.array(best_chromosome)
    print("Final weight:", sum(sum(optimal*itemWeights)))
    print("Final value score of backpack:", sum(sum(optimal*itemVals)))




    

