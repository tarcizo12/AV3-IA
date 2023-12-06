import numpy as np

def expressaoPrimeiraQuestao(x1,x2):
    return (x1*x1) + (x2*x2)

def expressaoSegundaQuestao(x1, x2):
    termo1 = np.exp(-((x1*x1) + (x2*x2)))
    termo2 = 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))
    resultado = termo1 + termo2
    return resultado

def terceiraExpressao(x1,x2):
    primeiroTermo = -20 * np.exp(-0.2 * (np.sqrt(0.5 * ((x1*x1) + (x2*x2))))) - np.exp(0.5 * ( np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)
    return primeiroTermo

def quartaExpressao(x1,x2):
    return