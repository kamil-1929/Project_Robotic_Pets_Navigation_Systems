import random
import numpy as np
from config import GRID_SIZE

POPULATION_SIZE = 50
GENES_LENGTH = None
MUTATION_RATE = 0.1
GENERATIONS = 100

def generate_individual(initial_path):
    return initial_path[:]

def generate_population(size, initial_path):
    return [generate_individual(initial_path) for _ in range(size)]

def fitness(individual, start, goal, static_obstacles, dynamic_obstacles):
    if len(individual) == 0 or individual[-1] != goal:
        return float('-inf')
    collisions = sum([1 for pos in individual if pos in static_obstacles or pos in dynamic_obstacles])
    path_length = len(individual)
    discontinuities = sum([1 for i in range(1, len(individual)) if abs(individual[i][0] - individual[i-1][0]) + abs(individual[i][1] - individual[i-1][1]) > 1])
    return max(0, -collisions - path_length - discontinuities * 10)  # Ensure non-negative fitness

def selection(population, fitnesses):
    indices = np.argsort(fitnesses)[::-1]
    return [population[i] for i in indices[:POPULATION_SIZE]]

def crossover(parent1, parent2):
    if len(parent1) < 2 or len(parent2) < 2:
        return parent1, parent2
    point = random.randint(1, min(len(parent1), len(parent2)) - 2)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(individual, grid_size):
    if random.random() < MUTATION_RATE:
        index = random.randint(0, len(individual) - 1)
        direction = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        new_pos = (individual[index][0] + direction[0], individual[index][1] + direction[1])
        if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:
            individual[index] = new_pos
    return individual

def genetic_algorithm(initial_path, start, goal, static_obstacles, dynamic_obstacles):
    global GENES_LENGTH
    GENES_LENGTH = len(initial_path)
    population = generate_population(POPULATION_SIZE, initial_path)
    best_individual = None
    best_fitness = -float('inf')

    for generation in range(GENERATIONS):
        fitnesses = [fitness(ind, start, goal, static_obstacles, dynamic_obstacles) for ind in population]
        best_fitness = max(fitnesses)
        best_individual = population[fitnesses.index(best_fitness)]

        selected_population = selection(population, fitnesses)
        next_generation = []
        for i in range(0, POPULATION_SIZE, 2):
            parent1 = selected_population[i]
            parent2 = selected_population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutate(child1, GRID_SIZE))
            next_generation.append(mutate(child2, GRID_SIZE))

        population = next_generation
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")

    return best_individual, best_fitness





