import Algoritmos
import Expressoes
import Graficos
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

VALOR_INVALIDO_MINIMIZACAO = 9999999999999999
VALOR_INVALIDO_MAXIMIZACAO = -VALOR_INVALIDO_MINIMIZACAO
R = 100


##MINIMIZAÇÃO 
def MainPrimeiraQuestao():

  primeiraExpressao = Expressoes.expressaoPrimeiraQuestao

  dominioPrimeiraQuestao = [-100 , 100]
  dadosResultadosMinimizacaoHillClimbing = []
  valorMinresultadoOtimoMinimiazacao = VALOR_INVALIDO_MINIMIZACAO
  
  for i in range(R):
    resultadoMinimizacaoHillClimbing = Algoritmos.hillClimbing(dominioPrimeiraQuestao, primeiraExpressao, True)
    
    if resultadoMinimizacaoHillClimbing[1] < valorMinresultadoOtimoMinimiazacao:
      valorMinresultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing[1]
      resultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing
      
    dadosResultadosMinimizacaoHillClimbing.append(resultadoMinimizacaoHillClimbing)

  if(resultadoOtimoMinimiazacao == VALOR_INVALIDO_MINIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  Graficos.imprimirGraficoDominioSimples(resultadoOtimoMinimiazacao, primeiraExpressao, dominioPrimeiraQuestao)


##MAXIMIZAÇÃO
def MainSegundaQuestao():
  segundaExpressao = Expressoes.expressaoSegundaQuestao
  dominiosSegundaQuestao = [[-2,4] , [-2,5]]
  dadosResultadosMaximizacaoHillClimbing = []
  valorMaxResultadoOtimoMinimiazacaoHillClimbing = VALOR_INVALIDO_MAXIMIZACAO
  
  for i in range(R):
    resultadoMaximizacaoHillClimbing = Algoritmos.hillClimbing(dominiosSegundaQuestao, segundaExpressao, False)

    if resultadoMaximizacaoHillClimbing[1] > valorMaxResultadoOtimoMinimiazacaoHillClimbing:
      valorMaxResultadoOtimoMinimiazacaoHillClimbing = resultadoMaximizacaoHillClimbing[1]
      resultadoOtimoMaximizacao = resultadoMaximizacaoHillClimbing
      
    dadosResultadosMaximizacaoHillClimbing.append(resultadoMaximizacaoHillClimbing)


  if(resultadoOtimoMaximizacao == VALOR_INVALIDO_MAXIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da Maximizacao" , resultadoOtimoMaximizacao)
  Graficos.imprimirGraficoDominioComposto(resultadoOtimoMaximizacao , segundaExpressao, dominiosSegundaQuestao)

##MINIMIZAÇÃO
def MainTerceiraQuestao():
  terceiraExpressao = Expressoes.terceiraExpressao
  dominiosTerceiraQuestao = [-8,8]

  dadosResultadosMinimizacaoHillClimbing = []
  valorMinresultadoOtimoMinimiazacao = VALOR_INVALIDO_MINIMIZACAO
  
  for i in range(R):
    resultadoMinimizacaoHillClimbing = Algoritmos.hillClimbing(dominiosTerceiraQuestao, terceiraExpressao, True)
    
    if resultadoMinimizacaoHillClimbing[1] < valorMinresultadoOtimoMinimiazacao:
      valorMinresultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing[1]
      resultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing
      
    dadosResultadosMinimizacaoHillClimbing.append(resultadoMinimizacaoHillClimbing)
    print(resultadoOtimoMinimiazacao)

  if(resultadoOtimoMinimiazacao == VALOR_INVALIDO_MINIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  Graficos.imprimirGraficoDominioSimples(resultadoOtimoMinimiazacao, terceiraExpressao, dominiosTerceiraQuestao)


#MINIMIZACAO
def MainQuartaQuestao():
  return
  # quartaExpressao = Expressoes.quartaExpressao
  # dominiosTerceiraQuestao = [-8,8]

  # dadosResultadosMinimizacaoHillClimbing = []
  # valorMinresultadoOtimoMinimiazacao = VALOR_INVALIDO_MINIMIZACAO
  
  # for i in range(R):
  #   resultadoMinimizacaoHillClimbing = Algoritmos.hillClimbing(dominiosTerceiraQuestao, quartaExpressao, True)
    
  #   if resultadoMinimizacaoHillClimbing[1] < valorMinresultadoOtimoMinimiazacao:
  #     valorMinresultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing[1]
  #     resultadoOtimoMinimiazacao = resultadoMinimizacaoHillClimbing
      
  #   dadosResultadosMinimizacaoHillClimbing.append(resultadoMinimizacaoHillClimbing)
  #   print(resultadoOtimoMinimiazacao)

  # if(resultadoOtimoMinimiazacao == VALOR_INVALIDO_MINIMIZACAO):
  #   raise ValueError("Não foi possivel determinar o valor otimo.")


  # ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DA RODADA: -> ", resultado)
  # print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  # Graficos.imprimirGraficoDominioSimples(resultadoOtimoMinimiazacao, quartaExpressao)



print('Trabalho de AV3')
MainPrimeiraQuestao()  
#MainSegundaQuestao()
#MainTerceiraQuestao()