qntDeDominiosAceitos = 2
import random
import numpy as np


def candidato(xbest, epsilon):
    # Gera um candidato aleatório na vizinhança de xbest
    return xbest + random.uniform(-epsilon, epsilon)


def restricao_caixa(x, limite_inferior, limite_superior):
    return np.maximum(limite_inferior, np.minimum(x, limite_superior))

def hillClimbing(
        dominios, funcao, 
        epsilon=0.1, maxit=1000, maxn=10, t_sem_melhoria=1000
    ):
    
    qntDeDominiosAceitos = 2

    if len(dominios) == qntDeDominiosAceitos:
        limite_inferior, limite_superior = dominios[0], dominios[1]

        x1 = np.random.uniform(low=limite_inferior, high=limite_superior)
        x2 = np.random.uniform(low=limite_inferior, high=limite_superior)

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
                x1_candidate = restricao_caixa(candidato(xbest[0], epsilon), limite_inferior, limite_superior)
                x2_candidate = restricao_caixa(candidato(xbest[1], epsilon), limite_inferior, limite_superior)

                y = [x1_candidate , x2_candidate]

                # Avalia a função no candidato
                F = funcao(y[0], y[1])

                if F < fbest:
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

    

