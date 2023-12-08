import random
import time

def initialize_population(population_size, board_size):
    return [[random.randint(0, board_size - 1) for _ in range(board_size)] for _ in range(population_size)]

def fitness(individual):
    pairs_attacking = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j] or abs(i - j) == abs(individual[i] - individual[j]):
                pairs_attacking += 1
    return 28 - pairs_attacking

def select_parents_roulette(population, num_parents):
    fitness_scores = [fitness(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    relative_fitness = [score / total_fitness for score in fitness_scores]

    parents = []
    for _ in range(num_parents):
        r = random.random()
        cumulative_probability = 0
        for i, prob in enumerate(relative_fitness):
            cumulative_probability += prob
            if r <= cumulative_probability:
                parents.append(population[i])
                break
    return parents

def crossover_one_point(parents):
    parent1, parent2 = parents
    crossover_point = random.randint(1, len(parent1) - 1)
    return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]

def crossover_two_points(parents):
    parent1, parent2 = parents
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    return parent1[:point1] + parent2[point1:point2] + parent1[point2:], parent2[:point1] + parent1[point1:point2] + parent2[point2:]

def mutate(individual, mutation_rate):
    return [random.randint(0, len(individual) - 1) if random.random() < mutation_rate else gene for gene in individual]


def genetic_algorithm_part1(board_size, population_size, num_generations, mutation_rate):
    start_time = time.time()
    population = initialize_population(population_size, board_size)
    found_solutions = set()

    for generation in range(num_generations):
        fitness_scores = [fitness(individual) for individual in population]
        num_parents = len(population) // 2
        parents = select_parents_roulette(population, num_parents)

        next_generation = []
        while len(next_generation) < population_size:
            selected_parents = random.sample(parents, 2)
            
            # Aplicar crossover com uma chance entre 85% e 95%
            if random.uniform(0, 1) < random.uniform(0.85, 0.95):
                child1, child2 = crossover_one_point(selected_parents)
            else:
                child1, child2 = selected_parents[0][:], selected_parents[1][:]

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        population = next_generation[:population_size]
        for individual in population:
            if fitness(individual) == 28 and tuple(individual) not in found_solutions:
                found_solutions.add(tuple(individual))

        if len(found_solutions) == 92:
            break
        print(f"Parte 1: Geração {generation + 1}, Soluções encontradas: {len(found_solutions)}")

    end_time = time.time()
    with open("solutions_first_loop.txt", "w") as file:
        for solution in found_solutions:
            file.write(f"{solution}\n")

    print(f"Parte 1 Concluída: {len(found_solutions)} soluções encontradas em {end_time - start_time} segundos")
    return found_solutions

def genetic_algorithm_part2(board_size, population_size, mutation_rate):
    start_time = time.time()
    population = initialize_population(population_size, board_size)
    found_solutions = set()
    count = 0

    while len(found_solutions) < 92:
        fitness_scores = [fitness(individual) for individual in population]
        num_parents = len(population) // 2
        parents = select_parents_roulette(population, num_parents)

        next_generation = []
        while len(next_generation) < population_size:
            selected_parents = random.sample(parents, 2)
            
            # Aplicar crossover com uma chance entre 85% e 95%
            if random.uniform(0, 1) < random.uniform(0.85, 0.95):
                child1, child2 = crossover_one_point(selected_parents)
            else:
                child1, child2 = selected_parents[0][:], selected_parents[1][:]

            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        population = next_generation[:population_size]
        for individual in population:
            if fitness(individual) == 28 and tuple(individual) not in found_solutions:
                found_solutions.add(tuple(individual))

        print(f"Parte 2: Geração {count}, Soluções encontradas: {len(found_solutions)}")
        count += 1

    end_time = time.time()
    with open("total_execution_and_solutions.txt", "w") as file:
        file.write(f"Tempo Total de Execução: {end_time - start_time} segundos\n")
        for solution in found_solutions:
            file.write(f"{solution}\n")

    print(f"Parte 2 Concluída: Todas as 92 soluções encontradas em {end_time - start_time} segundos")
    return found_solutions


# Parâmetros do Algoritmo Genético
board_size = 8
population_size = 100
num_generations = 10000  # Valor inicial para o critério de parada
mutation_rate = 0.01

# Executar a Parte 1 do Algoritmo Genético
solutions_part1 = genetic_algorithm_part1(board_size, population_size, num_generations, mutation_rate)

# Executar a Parte 2 do Algoritmo Genético
solutions_part2 = genetic_algorithm_part2(board_size, population_size, mutation_rate)