import random

def calculate_fitness(queen_positions):
    horizontal_collisions = sum([queen_positions.count(position)-1 for position in queen_positions]) / 2
    diagonal_collisions = 0

    board_size = len(queen_positions)
    left_diagonals = [0] * 2 * board_size
    right_diagonals = [0] * 2 * board_size

    for i in range(board_size):
        left_diagonals[i + queen_positions[i] - 1] += 1
        right_diagonals[board_size - i + queen_positions[i] - 2] += 1

    for i in range(2 * board_size - 1):
        diagonal_conflict_count = 0
        if left_diagonals[i] > 1:
            diagonal_conflict_count += left_diagonals[i] - 1
        if right_diagonals[i] > 1:
            diagonal_conflict_count += right_diagonals[i] - 1
        diagonal_collisions += diagonal_conflict_count / (board_size - abs(i - board_size + 1))
    
    return int(max_fitness - (horizontal_collisions + diagonal_collisions))

def calculate_probability(chromosome, calculate_fitness):
    return calculate_fitness(chromosome) / max_fitness

def select_random_chromosome(population, fitness_probabilities):
    population_with_probability = zip(population, fitness_probabilities)
    total_probability = sum(probability for _, probability in population_with_probability)
    random_selection = random.uniform(0, total_probability)
    accumulated_probability = 0

    for chromosome, probability in zip(population, fitness_probabilities):
        if accumulated_probability + probability >= random_selection:
            return chromosome
        accumulated_probability += probability
    assert False, "Random selection failed"

def crossover(chromosome1, chromosome2, crossover_probability):
    chromosome_length = len(chromosome1)
    if random.random() < crossover_probability:
        crossover_point = random.randint(0, chromosome_length - 1)
        return chromosome1[:crossover_point] + chromosome2[crossover_point:]
    else:
        return chromosome1

def mutate(chromosome):  
    chromosome_length = len(chromosome)
    mutation_point = random.randint(0, chromosome_length - 1)
    new_value = random.randint(1, chromosome_length)
    chromosome[mutation_point] = new_value
    return chromosome

def genetic_algorithm(population, calculate_fitness, crossover_probability):
    mutation_probability = 0.01
    new_population = []
    fitness_probabilities = [calculate_probability(chromosome, calculate_fitness) for chromosome in population]

    for i in range(len(population)):
        parent1 = select_random_chromosome(population, fitness_probabilities)
        parent2 = select_random_chromosome(population, fitness_probabilities)
        offspring = crossover(parent1, parent2, crossover_probability)
        if random.random() < mutation_probability:
            offspring = mutate(offspring)
        new_population.append(offspring)
        if calculate_fitness(offspring) == max_fitness:
            return new_population, True
    return new_population, False

def print_queen_positions(queen_positions):
    print("Queen Positions = {},  Fitness = {}"
        .format(str(queen_positions), calculate_fitness(queen_positions)))

if __name__ == "__main__":
    number_of_queens = 8
    max_fitness = (number_of_queens * (number_of_queens - 1)) / 2
    population_size = 100
    max_generations = 100000
    crossover_probability = random.uniform(0.85, 0.95)

    population = [[random.randint(1, number_of_queens) for _ in range(number_of_queens)] for _ in range(population_size)]
    current_generation = 1
    optimal_solution_found = False

    while current_generation <= max_generations and not optimal_solution_found:
        print("Generation = {}".format(current_generation), "Maximum Fitness = {}".format(max([calculate_fitness(positions) for positions in population])), "Queen Positions = {}".format(population[0]))
        population, optimal_solution_found = genetic_algorithm(population, calculate_fitness, crossover_probability)
        current_generation += 1

    if optimal_solution_found:
        print("Optimal Solution Found in Generation {}!".format(current_generation - 1))
        for queen_positions in population:
            if calculate_fitness(queen_positions) == max_fitness:
                print("One of the optimal solutions: ")
                print_queen_positions(queen_positions)

                chessboard = [["x"] * number_of_queens for _ in range(number_of_queens)]
                for i in range(number_of_queens):
                    chessboard[number_of_queens - queen_positions[i]][i] = "Q"

                print("Chessboard Configuration:")
                for row in chessboard:
                    print(" ".join(row))
    else:
        print("Optimal solution not found within the generation limit.")
