import random

# Parâmetros do Algoritmo
POPULATION_SIZE = 100
MAX_GENERATIONS = 500
CROSSOVER_RATE = 0.85  # Taxa de crossover ajustada
# CROSSOVER_RATE = random.uniform(0.85, 0.95)  # Taxa de crossover ajustada
MUTATION_RATE = 0.01
N_QUEENS = 8
MAX_FITNESS = (N_QUEENS * (N_QUEENS - 1)) // 2  # Número máximo de pares não atacantes

def initialize_population(pop_size):
    return [[random.randint(0, 7) for _ in range(N_QUEENS)] for _ in range(pop_size)]

def fitness(individual):
    non_attacking_pairs = 0
    for i in range(len(individual)):
        for j in range(i+1, len(individual)):
            if individual[i] != individual[j] and \
               individual[i] + i != individual[j] + j and \
               individual[i] - i != individual[j] - j:
                non_attacking_pairs += 1
    return non_attacking_pairs

def select(population):
    """ Seleção baseada no método da roleta. """
    fitness_sum = sum(fitness(individual) for individual in population)
    selection_probs = [fitness(individual) / fitness_sum for individual in population]
    return random.choices(population, weights=selection_probs, k=2)

def crossover(parent1, parent2):
    """ Realiza o crossover de dois pontos entre dois pais. """
    if random.random() < CROSSOVER_RATE:
        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
        return (parent1[:point1] + parent2[point1:point2] + parent1[point2:],
                parent2[:point1] + parent1[point1:point2] + parent2[point2:])
    return parent1, parent2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(individual) - 1)
        individual[idx] = random.randint(0, 7)
    return individual

# Algoritmo Genético
population = initialize_population(POPULATION_SIZE)
unique_solutions = set()

generation = 0
while len(unique_solutions) < 92:
    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1, parent2 = select(population)
        child1, child2 = crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])

    population = sorted(new_population, key=lambda ind: fitness(ind), reverse=True)

    # Atualiza o conjunto de soluções únicas
    for individual in population:
        if fitness(individual) == MAX_FITNESS:
            unique_solutions.add(tuple(individual))

    # Debugging: Melhor aptidão e diversidade da população
    best_fitness = fitness(population[0])
    unique_individuals = len(set(map(tuple, population)))
    print(f"Geração {generation}: Melhor Aptidão = {best_fitness}, Diversidade = {unique_individuals},                              Soluções Únicas = {len(unique_solutions)}")

    generation += 1

print("Número de soluções únicas encontradas:", len(unique_solutions))





# # Algoritmo Genético
# population = initialize_population(POPULATION_SIZE)
# unique_solutions = set()

# for generation in range(MAX_GENERATIONS):
#     new_population = []
#     for _ in range(POPULATION_SIZE // 2):
#         parent1, parent2 = select(population)
#         child1, child2 = crossover(parent1, parent2)
#         new_population.extend([mutate(child1), mutate(child2)])

#     population = sorted(new_population, key=lambda ind: fitness(ind), reverse=True)

#     # Debugging: Melhor aptidão e diversidade da população
#     best_fitness = fitness(population[0])
#     unique_individuals = len(set(map(tuple, population)))
#     if best_fitness >= 27:
#         print(f"Geração {generation}: Melhor Aptidão = {best_fitness}, Diversidade = {unique_individuals}")

#     # Atualiza o conjunto de soluções únicas
#     for individual in population:
#         if fitness(individual) == MAX_FITNESS:
#             unique_solutions.add(tuple(individual))
#             if len(unique_solutions) >= 92:
#                 break

#     if len(unique_solutions) >= 92:
#         break

# print("Número de soluções únicas encontradas:", len(unique_solutions))
