qntDeDominiosAceitos = 2
import random
import numpy as np
import Graficos
from numbers import Number

ALGORITIMOS_IMPLEMENTADOS = {
    'hillClimbing' : 1,
    'localRandomSearch': 2,
    'globalRandomSearch': 3,
    'simulatedAnnealing': 4
}


def candidato(xbest, epsilon):
    # Gera um candidato aleatório na vizinhança de xbest
    return xbest + random.uniform(-epsilon, epsilon)


def restricao_caixa(x, limite_inferior, limite_superior):
    return np.maximum(limite_inferior, np.minimum(x, limite_superior))

def getLimites(domino):
    ehDominoSimples = isinstance(domino[0], Number)
    ehDominioComposto = isinstance(domino[0], list)
    
    if(ehDominoSimples):
        limiteSuperiorX1    = domino[1]
        limiteInferiorX1    = domino[0]
        limiteSuperiorX2    = domino[1]
        limiteInferiorX2    = domino[0]

        return limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2
    
    elif(ehDominioComposto):
        limiteSuperiorX1    = domino[0][1]
        limiteInferiorX1    = domino[0][0]
        limiteSuperiorX2    = domino[0][1]
        limiteInferiorX2    = domino[0][0]


        return limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2

def hillClimbing(
        dominios, funcao, ehMinimizacao,
        epsilon=0.1, maxit=1000, maxn=5, t_sem_melhoria=1000,
    ):
    
    qntDeDominiosAceitos = 2

    if len(dominios) == qntDeDominiosAceitos:
        limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = getLimites(dominios)
        x1 = np.random.uniform(low=limiteInferiorX1, high=limiteSuperiorX1)
        x2 = np.random.uniform(low=limiteInferiorX2, high=limiteSuperiorX2)

        # Inicialização
        xbest = [x1, x2]
        fbest = funcao(x1, x2)

        i = 0
        t = 0  # Contador para verificar melhoria a cada t iterações

        
        while i < maxit and t < t_sem_melhoria:
            j = 0
            melhoria = False

            while j < maxn:
                j += 1
                # Gera um candidato
                x1_candidate = restricao_caixa(candidato(xbest[0], epsilon), limiteInferiorX1, limiteSuperiorX1)
                x2_candidate = restricao_caixa(candidato(xbest[1], epsilon), limiteInferiorX2, limiteSuperiorX2)

                y = [x1_candidate , x2_candidate]

                # Avalia a função no candidato
                F = funcao(y[0], y[1])

                # Atualiza xbest e fbest se necessário
                if (ehMinimizacao and F < fbest) or (not ehMinimizacao and F > fbest):
                    xbest = y
                    fbest = F
                    melhoria = True
                    break

            i += 1

            # Verifica se houve melhoria a cada t iterações
            if melhoria:
                t = 0
            else:
                t += 1
        return xbest, fbest

    else:
        raise ValueError("A função deve ter os domínios definidos.")

def localRandomSearch(
    dominios, funcao, ehMinimizacao,
    sigma=0.1, maxit=1000, maxn=5, t_sem_melhoria=1000,
):
    qntDeDominiosAceitos = 2

    if len(dominios) == qntDeDominiosAceitos:
        limiteSuperiorX1, limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = getLimites(dominios)

        # Inicialização
        x1 = np.random.uniform(low=limiteInferiorX1, high=limiteSuperiorX1)
        x2 = np.random.uniform(low=limiteInferiorX2, high=limiteSuperiorX2)

        xbest = [x1,x2] 
        fbest = funcao(*xbest)

        i = 0
        t = 0  # Contador para verificar melhoria a cada t iterações

        while i < maxit and t < t_sem_melhoria:
            j = 0
            melhoria = False

            while j < maxn:
                j += 1
                # Gera um perturbação aleatória
                perturbacao = np.random.normal(0, sigma, size=2)

                # Gera um candidato
                xcand = (xbest[0] + perturbacao[0], xbest[1] + perturbacao[1])
                
                # Restringe o candidato aos limites
                xcand = (
                    restricao_caixa(xcand[0], limiteInferiorX1, limiteSuperiorX1),
                    restricao_caixa(xcand[1], limiteInferiorX2, limiteSuperiorX2)
                )

                # Avalia a função no candidato
                fcand = funcao(*xcand)

                # Atualiza xbest e fbest se necessário
                if (ehMinimizacao and fcand < fbest) or (not ehMinimizacao and fcand > fbest):
                    xbest = xcand
                    fbest = fcand
                    melhoria = True
                    break

            i += 1

            # Verifica se houve melhoria a cada t iterações
            if melhoria:
                t = 0
            else:
                t += 1

        return xbest, fbest

    else:
        raise ValueError("A função deve ter os domínios definidos.")

def globalRandomSearch(
    dominios, funcao, ehMinimizacao,
    maxit=1000, t_sem_melhoria=1000,
):
    qntDeDominiosAceitos = 2

    if len(dominios) == qntDeDominiosAceitos:
        limiteSuperiorX1, limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = getLimites(dominios)

        # Inicialização
        x1 = np.random.uniform(low=limiteInferiorX1, high=limiteSuperiorX1)
        x2 = np.random.uniform(low=limiteInferiorX2, high=limiteSuperiorX2)
        xbest = [x1, x2] 
        fbest = funcao(*xbest)

        i = 0
        t = 0  # Contador para verificar melhoria a cada t iterações

        while i < maxit and t < t_sem_melhoria:
            # Gera um candidato
            xcand = np.random.uniform(low=limiteInferiorX1, high=limiteSuperiorX1), np.random.uniform(low=limiteInferiorX2, high=limiteSuperiorX2)

            # Avalia a função no candidato
            fcand = funcao(*xcand)

            # Atualiza xbest e fbest se necessário
            if (ehMinimizacao and fcand < fbest) or (not ehMinimizacao and fcand > fbest):
                xbest = xcand
                fbest = fcand
                t = 0  # Reseta o contador de iterações sem melhoria
            else:
                t += 1

            i += 1

        return xbest, fbest

    else:
        raise ValueError("A função deve ter os domínios definidos.")

def simulatedAnnealing(
    dominios, funcao, ehMinimizacao,
    T0=100, maxit=1000, sigma=0.1, pm=0.5, eta=0.1, maxn=5, t_sem_melhoria=1000,
):
    qntDeDominiosAceitos = 2

    if len(dominios) == qntDeDominiosAceitos:
        limiteSuperiorX1, limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = getLimites(dominios)

        # Inicialização
        x1 = np.random.uniform(low=limiteInferiorX1, high=limiteSuperiorX1)
        x2 = np.random.uniform(low=limiteInferiorX2, high=limiteSuperiorX2)
        xbest = [x1,x2] 
        fbest = funcao(*xbest)

        i = 0
        t = 0  # Contador para verificar melhoria a cada t iterações
        T = T0  # Temperatura inicial

        while i < maxit and t < t_sem_melhoria:
            j = 0
            melhoria = False

            while j < maxn:
                j += 1
                # Gera um perturbação aleatória
                perturbacao = np.random.normal(0, sigma, size=2)

                # Gera um candidato
                xcand = (xbest[0] + perturbacao[0], xbest[1] + perturbacao[1])

                # Restringe o candidato aos limites
                xcand = (
                    restricao_caixa(xcand[0], limiteInferiorX1, limiteSuperiorX1),
                    restricao_caixa(xcand[1], limiteInferiorX2, limiteSuperiorX2)
                )

                # Avalia a função no candidato
                fcand = funcao(*xcand)

                # Atualiza xbest e fbest com probabilidade
                if (ehMinimizacao and fcand < fbest) or (not ehMinimizacao and fcand > fbest):
                    xbest = xcand
                    fbest = fcand
                    melhoria = True
                    break
                elif np.random.rand() < np.exp(-(fcand - fbest) / T):
                    xbest = xcand
                    fbest = fcand

            i += 1

            # Verifica se houve melhoria a cada t iterações
            if melhoria:
                t = 0
            else:
                t += 1

            # Escalona a temperatura
            T = cooling_schedule(T)

        return xbest, fbest

    else:
        raise ValueError("A função deve ter os domínios definidos.")

def cooling_schedule(T):
    alpha = 0.9  # Fator de resfriamento
    return alpha * T
