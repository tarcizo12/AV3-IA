import numpy as np

def expressaoPrimeiraQuestao(x1,x2):
    return (x1*x1) + (x2*x2)

def expressaoSegundaQuestao(x1, x2):
    primeiroTermo = np.exp(-((x1*x1) + (x2*x2)))
    segundoTermo = 2 * np.exp(-((x1 - 1.7)**2 + (x2 - 1.7)**2))

    return primeiroTermo + segundoTermo

def terceiraExpressao(x1,x2):
    termo = -20 * np.exp(-0.2 * (np.sqrt(0.5 * ((x1*x1) + (x2*x2))))) - np.exp(0.5 * ( np.cos(2 * np.pi * x1) + np.cos(2 * np.pi * x2))) + 20 + np.exp(1)

    return termo

def quartaExpressao(x1,x2):
    primeiroTermo = (x1*x1) - 10*np.cos(2*np.pi*x1) + 10 
    segundoTermo = ((x2*x2) - 10*np.cos(2*np.pi*x2) + 10) 

    return primeiroTermo + segundoTermo

def quintaExpressao(x1,x2):
    termo = ((x1 - 1)*( x1- 1)) + 100*( (x2 - (x1*x1))*(x2 - (x1*x1)) )
    return termo

def sextaExpressao(x1,x2):
    termo = (x1*np.sin(4*np.pi*x1)) - (x2*np.sin( (4*np.pi*x2) + np.pi)) + 1
    return termo

def setimaExpressao(x1,x2):
    return (-np.sin(x1) * np.power(np.sin((x1 * 2) / np.pi), 2) * 1e-10) + (-np.sin(x2) * np.power(np.sin((2 * x2 * 2) / np.pi), 2) * 1e-10)

def oitavaExpressao(x1,x2):
    modulo1 = np.abs(x1 / 2 + (x2 + 47))
    modulo2 = np.abs(x1 - (x2 + 47))
    primeiroTermo = -(x1 + 47)*np.sin(np.sqrt(modulo1))
    segundoTermo = x1*np.sin(np.sqrt(modulo2))

    return primeiroTermo - segundoTermo