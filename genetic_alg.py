import numpy as np
import random as rd
from random import *

# main driver of the genetic algorithm, returns the optimal chromosome 
# representing which items to bring
def genetic_algorithm(initialPopulation, weightArr, valueArr, numGenerations, 
                        maxWeight): 
    optimal_chrom = []
    numParents = 8
    numChildren = 8

    for i in range(numGenerations):
        fitness_arr = fitness_function(weightArr, valueArr, initialPopulation,
                                         maxWeight)
        parents = select_parents(fitness_arr, numParents, initialPopulation)
        offsprings = recombination(parents, numChildren)
        mutants = mutation(offsprings)
        initialPopulation[0:parents.shape[0]] = parents
        initialPopulation[parents.shape[0]:] = mutants

    final_fitness = fitness_function(weightArr, valueArr, initialPopulation, 
                                        maxWeight)
    max = np.where(final_fitness == np.max(final_fitness))
    optimal_chrom.append(initialPopulation[max[0][0]])
    return optimal_chrom
        
# selects the numParents best individuals from the population to be parents of
# the next generation
def select_parents(fitness_arr, numParents, population):
    parents = np.empty((numParents, population.shape[1]))
    for i in range(numParents):
        maxFit = np.where(fitness_arr == np.max(fitness_arr))
        parents[i] = population[maxFit[0][0]]
        fitness_arr[maxFit[0][0]] = 0
    return parents   

# gets fitness of given population based on the values and weights of objects
# if total weight exceeds maxWeight, score decreases by factor of 10
def fitness_function(weightArr, valueArr, population, maxWeight):
    fitness_arr = np.empty(population.shape[0])
    for i in range(population.shape[0]):
        total_value = sum(population[i] * valueArr)
        total_weight = sum(population[i] * weightArr)
        if total_weight <= maxWeight:
            fitness_arr[i] = total_value
        else:
            fitness_arr[i] = total_value / 10
    return fitness_arr

# does a crossover of one child given two parents and a randomly previously 
# selected cross_point
def crossover(parent1, parent2, cross_point):
    result = np.empty(parent1.shape[0])
    result[0:cross_point] = parent1[0:cross_point]
    result[cross_point:] = parent2[cross_point:]
    return result

# given parents and children, randomizes chromosomes of individuals based off
# a randomly selected cross_point
def recombination(parents, numChildren):
    offspring = np.empty((numChildren, parents.shape[1]))
    for i in range(numChildren):
        cross_pt = randint(4,8)
        parent1_index = randint(0, parents.shape[0]-1)
        parent2_index = parent1_index
        while parent1_index == parent2_index:
            parent2_index = randint(0, parents.shape[0]-1)
        offspring[i] = crossover(parents[parent1_index], parents[parent2_index],
                                    cross_pt)
    return offspring  

# randomly selects individuals' chromosomes from the population to mutate
# gene to mutate is random as well
def mutation(children):
    mutants = np.empty(children.shape)
    mutationRate = 75
    rand = randint(0,100)
    
    for i in range(mutants.shape[0]):
        mutants[i] = children[i]
        if rand > mutationRate:
            continue
        # randomly chosen gene to mutate
        mutatedGene = randint(0,11)   
        if mutants[i,mutatedGene] == 0 :
            mutants[i,mutatedGene] = 1
        else :
            mutants[i,mutatedGene] = 0
    return mutants
