import numpy as np
import random
import matplotlib.pyplot as plt

def distance(p1, p2):    
    return np.sqrt(np.sum((p1 - p2)**2))

def generate_points(N):
    # Gera N pontos aleatórios em um espaço 2D
    points = np.random.rand(N, 2) * 100  # Multiplica por 100 para espalhar os pontos em uma área maior
    return points

def fitness(route, points):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(points[route[i]], points[route[i + 1]])
    total_distance += distance(points[route[-1]], points[route[0]])  # Retornar ao ponto de partida
    return total_distance

def tournament_selection(population, fitnesses, tournament_size=3):
    winners = []
    for _ in range(2):
        tournament = random.sample(list(enumerate(population)), tournament_size)
        winner = min(tournament, key=lambda ind: fitnesses[ind[0]])[1]
        winners.append(winner)
    return winners

def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(len(parent1)), 2))
    middle1 = parent1[point1:point2]
    child1 = [city for city in parent2 if city not in middle1]  # Remove as cidades do meio do parent1
    child1[point1:point1] = middle1  # Insere as cidades do meio na posição correta
    # Repita para o segundo filho
    middle2 = parent2[point1:point2]
    child2 = [city for city in parent1 if city not in middle2]
    child2[point1:point1] = middle2
    return [child1, child2]



def mutate(route):
    if len(route) > 1 and random.random() < 0.01:  # Probabilidade de mutação
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


# Parâmetros do Algoritmo
N_pontos = 50  # Número de pontos por região
NUM_CITIES = N_pontos
POPULATION_SIZE = 100  # Exemplo de tamanho da população
MAX_GENERATIONS = 500  # Exemplo de número máximo de gerações
points = generate_points(N_pontos)
population = [random.sample(range(NUM_CITIES), NUM_CITIES) for _ in range(POPULATION_SIZE)]

best_route = None
best_fitness = float('inf')
convergencia = 0
iteracoes_sem_melhora = 100

for generation in range(MAX_GENERATIONS):
    fitnesses = [fitness(route, points) for route in population]

    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1, parent2 = tournament_selection(population, fitnesses)
        child1, child2 = two_point_crossover(parent1, parent2)
        new_population.extend([mutate(child1), mutate(child2)])

    population = new_population

    # Atualizar a melhor solução
    generation_best_route = min(population, key=lambda route: fitness(route, points))
    generation_best_fitness = fitness(generation_best_route, points)
    if generation_best_fitness < best_fitness:
        best_fitness = generation_best_fitness
        best_route = generation_best_route
        convergencia = 0
    else:
        convergencia += 1

    if convergencia >= iteracoes_sem_melhora:
        break

    print(f"Geração {generation}: Melhor Distância = {best_fitness}")

print("Melhor rota encontrada:", best_route)
print("Distância da melhor rota:", best_fitness)
