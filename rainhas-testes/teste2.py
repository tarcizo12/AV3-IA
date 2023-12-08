import random
import time

# Parâmetros do Algoritmo
POPULATION_SIZE = 100
MIN_CROSSOVER_RATE = 0.85  # Taxa de crossover mínima
MAX_CROSSOVER_RATE = 0.95  # Taxa de crossover máxima
MUTATION_RATE = 0.01
N_QUEENS = 8
MAX_FITNESS = (N_QUEENS * (N_QUEENS - 1)) // 2  # Número máximo de pares não atacantes

def initialize_population(pop_size):
    return [[random.randint(0, 7) for _ in range(N_QUEENS)] for _ in range(pop_size)]

def fitness(individual):
    """ Retorna o número de pares não atacantes. """
    horizontal_collisions = sum([individual.count(queen) - 1 for queen in individual]) // 2
    diagonal_collisions = 0

    n = len(individual)
    left_diagonal = [0] * 2 * n
    right_diagonal = [0] * 2 * n
    for i in range(n):
        left_diagonal[i + individual[i] - 1] += 1
        right_diagonal[len(individual) - i + individual[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2 * n - 1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i] - 1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i] - 1
        diagonal_collisions += counter / (n - abs(i - n + 1))

    return int(MAX_FITNESS - (horizontal_collisions + diagonal_collisions))

def select(population):
    """ Seleção baseada no método da roleta. """
    fitness_sum = sum(fitness(individual) for individual in population)
    selection_probs = [fitness(individual) / fitness_sum for individual in population]
    return random.choices(population, weights=selection_probs, k=2)

def one_point_crossover(parent1, parent2):
    """ Realiza o crossover de um ponto entre dois pais. """
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, len(parent1) - 1)
        return (parent1[:point] + parent2[point:], parent2[:point] + parent1[point:])
    return parent1, parent2

def two_point_crossover(parent1, parent2):
    """ Realiza o crossover de dois pontos entre dois pais. """
    if random.random() < CROSSOVER_RATE:
        point1, point2 = sorted(random.sample(range(1, len(parent1)), 2))
        return (parent1[:point1] + parent2[point1:point2] + parent1[point2:], parent2[:point1] + parent1[point1:point2] + parent2[point2:])
    return parent1, parent2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx = random.randint(0, len(individual) - 1)
        individual[idx] = random.randint(0, len(individual) - 1)
    return individual

# Algoritmo Genético
start_time = time.time()  # Captura o tempo inicial
population = initialize_population(POPULATION_SIZE)
unique_solutions = []  # Lista para armazenar soluções únicas encontradas

generation = 0
CROSSOVER_RATE = MIN_CROSSOVER_RATE  # Taxa de crossover inicial

while len(unique_solutions) < 92:
    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1, parent2 = select(population)
        # Escolha entre um ponto ou dois pontos de recombinação
        if random.random() < 0.9:
            child1, child2 = one_point_crossover(parent1, parent2)
        # else:
        #     child1, child2 = two_point_crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])

    population = sorted(new_population, key=lambda ind: fitness(ind), reverse=True)

    # Aumente gradualmente a taxa de crossover
    CROSSOVER_RATE += 0.001

    # Atualiza a lista de soluções únicas
    for individual in population:
        if fitness(individual) == MAX_FITNESS and tuple(individual) not in unique_solutions:
            unique_solutions.append(tuple(individual))

    # Debugging: Melhor aptidão e diversidade da população
    best_fitness = fitness(population[0])
    unique_individuals = len(set(map(tuple, population)))
    print(f"Geração {generation}: Melhor Aptidão = {best_fitness}, Diversidade = {unique_individuals}, Soluções Únicas = {len(unique_solutions)}")
    with open("resultado.txt", "a") as file:
        file.write(f"Geração {generation}: Melhor Aptidão = {best_fitness}, Diversidade = {unique_individuals}, Soluções Únicas = {len(unique_solutions)}\n")
        
    generation += 1

# Após o algoritmo, calcule o tempo decorrido
end_time = time.time()
elapsed_time = end_time - start_time

# Abra um arquivo de texto para gravar as soluções únicas
with open("solucoes_unicas.txt", "w") as file:
    file.write(f"Tempo decorrido: {elapsed_time} segundos\n")
    file.write("Soluções únicas encontradas:\n")
    for solution in unique_solutions:
        file.write(f"{solution}\n")

print("Número de soluções únicas encontradas:", len(unique_solutions))
