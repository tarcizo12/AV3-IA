import random

def initialize_population(population_size, board_size):
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, board_size - 1) for _ in range(board_size)]
        population.append(individual)
    return population

def fitness(individual):
    # Contar o número de pares de rainhas que se atacam
    pairs_attacking = 0
    for i in range(len(individual)):
        for j in range(i + 1, len(individual)):
            if individual[i] == individual[j] or abs(i - j) == abs(individual[i] - individual[j]):
                pairs_attacking += 1
    return 28 - pairs_attacking

def select_parents_roulette(population, num_parents):
    # Cálculo da aptidão relativa
    fitness_scores = [fitness(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    relative_fitness = [score / total_fitness for score in fitness_scores]
    
    # Seleção de pais com base na roleta
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
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def crossover_two_points(parents):
    parent1, parent2 = parents
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.randint(0, len(individual) - 1)
    return individual

def genetic_algorithm(board_size, population_size, num_generations, mutation_rate):
    population = initialize_population(population_size, board_size)
    found_solutions = set()
    
    for generation in range(num_generations):
        # Avaliar a aptidão da população
        fitness_scores = [fitness(individual) for individual in population]
        avg_fitness = sum(fitness_scores) / len(fitness_scores)
        best_fitness = max(fitness_scores)

        # Debugging: Exibir informações de progresso
        print(f"Generation {generation + 1}: Average Fitness = {avg_fitness}, Best Fitness = {best_fitness}, Solutions = {len(found_solutions)}")
        
        # Selecionar pais usando o método da roleta
        num_parents = len(population) // 2
        parents = select_parents_roulette(population, num_parents)
        
        # Criar a próxima geração
        next_generation = []
        while len(next_generation) < population_size:
            selected_parents = random.sample(parents, 2)
            child1, child2 = crossover_one_point(selected_parents)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        # Atualizar a população e verificar soluções
        population = next_generation[:population_size]
        for individual in population:
            if fitness(individual) == 28 and tuple(individual) not in found_solutions:
                found_solutions.add(tuple(individual))

        # Critério de parada: verificar se todas as soluções foram encontradas
        if len(found_solutions) == 92:
            print("Todas as soluções encontradas.")
            return found_solutions

    # Continuação após atingir o critério de parada inicial
    print("Critério de parada inicial atingido. Continuando a busca por todas as soluções...")
    while len(found_solutions) < 92:
        # Selecionar pais usando o método da roleta
        num_parents = len(population) // 2
        parents = select_parents_roulette(population, num_parents)
        
        # Criar a próxima geração
        next_generation = []
        while len(next_generation) < population_size:
            selected_parents = random.sample(parents, 2)
            child1, child2 = crossover_one_point(selected_parents)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])
            
        # Atualizar a população e verificar soluções
        population = next_generation[:population_size]
        for individual in population:
            if fitness(individual) == 28 and tuple(individual) not in found_solutions:
                found_solutions.add(tuple(individual))
                
        # Debugging: Exibir informações de progresso
        print(f"Continuação: Solutions = {len(found_solutions)}")

    return found_solutions

# Parâmetros do Algoritmo Genético
board_size = 8
population_size = 100
num_generations = 10000  # Valor inicial para o critério de parada
mutation_rate = 0.01

# Executar o Algoritmo Genético
solutions_found = genetic_algorithm(board_size, population_size, num_generations, mutation_rate)
print(f"Encontradas {len(solutions_found)} soluções diferentes.")