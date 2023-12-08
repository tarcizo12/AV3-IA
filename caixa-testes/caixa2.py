import numpy as np
import matplotlib.pyplot as plt

def distance(p1, p2):    
    return np.sqrt(np.sum((p1 - p2)**2))

def generate_points(Npontos_por_regiao, Nregioes):
    pontos = []
    for i in range(Nregioes):
        x_partition = np.random.uniform(-10, 10, size=(Npontos_por_regiao, 3))
        y_partition = np.random.uniform(0, 20, size=(Npontos_por_regiao, 3))
        z_partition = np.random.uniform(-20, 0, size=(Npontos_por_regiao, 3))
        w_partition = np.random.uniform(0, 20, size=(Npontos_por_regiao, 3))

        x1 = np.array([[20, -20, -20]])
        x1 = np.tile(x1, (Npontos_por_regiao, 1))
        x_partition = x_partition + x1

        x1 = np.array([[-20, 20, 20]])
        x1 = np.tile(x1, (Npontos_por_regiao, 1))
        y_partition = y_partition + x1

        x1 = np.array([[-20, 20, -20]])
        x1 = np.tile(x1, (Npontos_por_regiao, 1))
        z_partition = z_partition + x1

        x1 = np.array([[20, 20, -20]])
        x1 = np.tile(x1, (Npontos_por_regiao, 1))
        w_partition = w_partition + x1
        
        pontos.extend(np.concatenate((x_partition, y_partition, z_partition, w_partition), axis=0))
        
    return np.array(pontos)

def total_distance(path, points):
    dist = 0
    for i in range(len(path) - 1):
        dist += distance(points[path[i]], points[path[i + 1]])
    dist += distance(points[path[-1]], points[path[0]])
    return dist

def tournament_selection(population, tournament_size, points):
    selected_parents = []
    while len(selected_parents) < len(population):
        tournament_candidates = np.random.choice(len(population), tournament_size, replace=False)
        tournament_costs = [total_distance(population[i], points) for i in tournament_candidates]
        best_candidate_index = tournament_candidates[np.argmin(tournament_costs)]
        selected_parents.append(population[best_candidate_index])
    return np.array(selected_parents)

def crossover(parent1, parent2):
    cut_point1, cut_point2 = sorted(np.random.choice(len(parent1), 2, replace=False))
    child1_middle = set(parent1[cut_point1:cut_point2])
    child2_middle = set(parent2[cut_point1:cut_point2])

    child1 = [p for p in parent2 if p not in child1_middle]
    child2 = [p for p in parent1 if p not in child2_middle]

    return np.array(child1[:cut_point1] + list(child1_middle) + child1[cut_point1:], dtype=int), \
           np.array(child2[:cut_point1] + list(child2_middle) + child2[cut_point1:], dtype=int)

def mutate(individual, mutation_rate):
    for _ in range(len(individual)):
        if np.random.rand() < mutation_rate:
            index1, index2 = np.random.choice(len(individual), 2, replace=False)
            individual[index1], individual[index2] = individual[index2], individual[index1]
    return individual

# Configurações do algoritmo
Npontos_por_regiao = 60
Nregioes = 4
N_populacao = 100
max_geracoes = 10000
tournament_size = 5
mutation_rate = 0.01
Ne = 10  # Número de indivíduos elitistas

# Critérios de parada
epsilon = 10
optimal_aptidao = 100000  # Valor ótimo da aptidão
melhoria_limite = 0.01  # Limite de melhoria para considerar uma mudança significativa
janela_melhoria = 20  # Número de gerações para monitorar a falta de melhoria
janela_estagnacao = 20  # Número de gerações para monitorar a estagnação genotípica
limite_estagnacao = 0.05  # Limite para a estagnação genotípica

# Geração de pontos e população inicial
points = generate_points(Npontos_por_regiao, Nregioes)
print("Pontos Gerados:", points.shape)
populacao = [np.random.permutation(len(points)) for _ in range(N_populacao)]

melhor_aptidao = float('inf')
aptidoes_anteriores = []
geracoes_solucoes_aceitaveis = []
historico_aptidao = []  # Para monitorar a evolução da aptidão
geracoes_sem_melhoria_atual = 0

# Loop principal do algoritmo genético
for geracao in range(max_geracoes):
    pais = tournament_selection(populacao, tournament_size, points)

    # Criação da prole
    prole = []
    for i in range(0, len(pais), 2):
        if i + 1 < len(pais):
            filho1, filho2 = crossover(pais[i], pais[i + 1])
            print("Crossover - Pai1:", len(pais[i]), "Pai2:", len(pais[i + 1]), "Filho1:", len(filho1), "Filho2:", len(filho2))
            prole.extend([filho1, filho2])

    # Aplicação de mutações
    for i in range(len(prole)):
        antes = len(prole[i])
        prole[i] = mutate(prole[i], mutation_rate)
        depois = len(prole[i])
        print("Mutação - Antes:", antes, "Depois:", depois)

    # Elitismo: manter os Ne melhores indivíduos
    populacao_ordenada = sorted(populacao, key=lambda ind: total_distance(ind, points))
    elitistas = populacao_ordenada[:Ne]

    # Substituir a pior parte da população pela elite e prole
    nova_populacao = elitistas + prole[:N_populacao - Ne]
    populacao = nova_populacao[:N_populacao]

    # Avaliação das aptidões
    aptidoes = [total_distance(individuo, points) for individuo in populacao]
    print("Aptidões:", aptidoes[:10])  # Imprime as 10 primeiras aptidões
    indice_melhor = np.argmin(aptidoes)
    historico_aptidao.append(aptidoes[indice_melhor])  # Adiciona a melhor aptidão à história

    # Verificação de critérios de parada
    if aptidoes[indice_melhor] <= (optimal_aptidao - epsilon):
        geracoes_solucoes_aceitaveis.append(geracao)

    if len(aptidoes_anteriores) > janela_estagnacao:
        del aptidoes_anteriores[0]
    aptidoes_anteriores.append(aptidoes[indice_melhor])

    if melhor_aptidao - aptidoes[indice_melhor] < melhoria_limite:
        geracoes_sem_melhoria_atual += 1
        if geracoes_sem_melhoria_atual >= janela_melhoria:
            print("Parando por falta de melhoria.")
            break
    else:
        geracoes_sem_melhoria_atual = 0
        melhor_aptidao = aptidoes[indice_melhor]

    if max(aptidoes_anteriores) - min(aptidoes_anteriores) < limite_estagnacao:
        break

    # Debug: Visualização dos resultados intermediários
    if geracao % 100 == 0:  # A cada 100 gerações
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='#248DD2', marker='o')
        ax.plot(points[populacao[indice_melhor], 0], points[populacao[indice_melhor], 1], points[populacao[indice_melhor], 2], c='red')
        plt.show()

# Análise da moda das gerações para soluções aceitáveis
if geracoes_solucoes_aceitaveis:
    moda_geracoes = max(set(geracoes_solucoes_aceitaveis), key=geracoes_solucoes_aceitaveis.count)
    print(f"A moda das gerações para soluções aceitáveis é: {moda_geracoes}")
else:
    print("Nenhuma solução aceitável encontrada.")

# Visualização da evolução da aptidão
plt.figure()
plt.plot(historico_aptidao)
plt.title("Evolução da Melhor Aptidão por Geração")
plt.xlabel("Geração")
plt.ylabel("Aptidão")
plt.show()  # Alterado para mostrar o gráfico imediatamente

# Visualização dos resultados finais
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(points[:, 0], points[:, 1], points[:, 2], c='#248DD2', marker='o')
ax.plot(points[populacao[indice_melhor], 0], points[populacao[indice_melhor], 1], points[populacao[indice_melhor], 2], c='red', marker='x', linewidth=3)
plt.tight_layout()
plt.show()  # Alterado para mostrar o gráfico imediatamente
