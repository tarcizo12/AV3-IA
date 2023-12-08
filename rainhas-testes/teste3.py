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

def genetic_algorithm(board_size, population_size, num_generations, mutation_rate, optimal_fitness=None):
    # Inicialize a população
    population = initialize_population(population_size, board_size)
    
    for generation in range(num_generations):
        # Avaliar a aptidão da população
        fitness_scores = [fitness(individual) for individual in population]
        best_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(best_fitness)]
        
        print(f"Generation {generation + 1}: Best Fitness = {best_fitness}")
        
        # Verificar se atingiu o valor ótimo da função custo (se aplicável)
        if optimal_fitness is not None and best_fitness >= optimal_fitness:
            break
        
        # Selecionar pais usando o método da roleta
        parents = select_parents_roulette(population, num_parents=population_size // 2)
        
        # Certifique-se de que existem dois pais
        if len(parents) != 2:
            continue
        
        child1, child2 = crossover_one_point(parents)
        
        # Mutação com probabilidade de 1%
        if random.uniform(0, 1) < 0.01:  # 1% de chance de mutação
            child1 = mutate(child1, mutation_rate)
        if random.uniform(0, 1) < 0.01:  # 1% de chance de mutação
            child2 = mutate(child2, mutation_rate)
        
        children.extend([child1, child2])
        
        # Substituir a população antiga pela nova
        population = children
    
    return best_individual

best_solution = genetic_algorithm(board_size=8, population_size=100, num_generations=1000, mutation_rate=0.01)
print("Best Solution:", best_solution)

