import Algoritmos
import Expressoes
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 


VALOR_INVALIDO = 9999999999999999


def Main():
  print('Trabalho de AV3')
  R = 1000

  primeiraExpressao = Expressoes.expressaoPrimeiraQuestao

  dominioPrimeiraQuestao = [-100, 100]
  dadosResultadosMinimizacaoHillClimbing = []
  resultadoOtimoMinimiazacao = VALOR_INVALIDO

  
  for i in range(R):
    resultado = Algoritmos.hillClimbing(dominioPrimeiraQuestao, primeiraExpressao)
    
    if resultado[1] < resultadoOtimoMinimiazacao:
      resultadoOtimoMinimiazacao = resultado[1]
      
    dadosResultadosMinimizacaoHillClimbing.append(resultado)

  if(resultadoOtimoMinimiazacao == VALOR_INVALIDO):
    raise ValueError("Não foi possivel ler valor otimo.")


  ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DO TREINO: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)

Main()  