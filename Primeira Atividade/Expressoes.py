import numpy as np

def expressaoPrimeiraQuestao(x1,x2):
    return (x1*x1) + (x2*x2)

def expressaoSegundaQuestao(x1, x2):
    termo1 = np.exp(-((x1*x1) + (x2*x2)))
    termo2 = 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))
    resultado = termo1 + termo2
    return resultado
