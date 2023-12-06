import Algoritmos
import Expressoes
import Graficos
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 

VALOR_INVALIDO_MINIMIZACAO = 9999999999999999
VALOR_INVALIDO_MAXIMIZACAO = -VALOR_INVALIDO_MINIMIZACAO
R = 100

def rodarAlgoritimoDeBusca(algoritimoDesejado):
  
  if algoritimoDesejado == Algoritmos.ALGORITIMOS_IMPLEMENTADOS['hillClimbing']:

    return Algoritmos.hillClimbing
  
  elif algoritimoDesejado == Algoritmos.ALGORITIMOS_IMPLEMENTADOS['localRandomSearch']:

    return Algoritmos.local_random_search


  return

##1. MINIMIZAÇÃO 
def MainPrimeiraQuestao(algoritimo):

  primeiraExpressao = Expressoes.expressaoPrimeiraQuestao

  dominioPrimeiraQuestao = [-100 , 100]
  dadosResultados = []
  valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
  for i in range(R):
    algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

    resultadoMinimizacao = algoritimoAtual(dominioPrimeiraQuestao, primeiraExpressao, True)
    
    if resultadoMinimizacao[1] < valorMinResultadoOtimo:
      valorMinResultadoOtimo = resultadoMinimizacao[1]
      resultadoOtimoMinimiazacao = resultadoMinimizacao
    
    print(resultadoMinimizacao)
    dadosResultados.append(resultadoMinimizacao)

  if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, primeiraExpressao, dominioPrimeiraQuestao, dadosResultados)

##2. MAXIMIZAÇÃO
def MainSegundaQuestao(algoritimo):
  segundaExpressao = Expressoes.expressaoSegundaQuestao
  dominiosSegundaQuestao = [[-2,4] , [-2,5]]
  dadosResulados = []
  valorMaxResultadotimo = VALOR_INVALIDO_MAXIMIZACAO
  
  for i in range(R):
    algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

    resultadoMaximizacao = algoritimoAtual(dominiosSegundaQuestao, segundaExpressao, False)

    if resultadoMaximizacao[1] > valorMaxResultadotimo:
      valorMaxResultadotimo = resultadoMaximizacao[1]
      resultadoOtimoMaximizacao = resultadoMaximizacao
      
    dadosResulados.append(resultadoMaximizacao)


  if(valorMaxResultadotimo == VALOR_INVALIDO_MAXIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da Maximizacao" , resultadoOtimoMaximizacao)
  Graficos.imprimirGrafico(resultadoOtimoMaximizacao , segundaExpressao, dominiosSegundaQuestao, dadosResulados)

##3. MINIMIZAÇÃO
def MainTerceiraQuestao(algoritimo):
  terceiraExpressao = Expressoes.terceiraExpressao
  dominiosTerceiraQuestao = [-8,8]

  dadosResultados = []
  valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
  for i in range(R):
    algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

    resultadoMinimizacao = algoritimoAtual(dominiosTerceiraQuestao, terceiraExpressao, True)
    
    if resultadoMinimizacao[1] < valorMinResultadoOtimo:
      valorMinResultadoOtimo = resultadoMinimizacao[1]
      resultadoOtimoMinimiazacao = resultadoMinimizacao
      
    dadosResultados.append(resultadoMinimizacao)

  if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, terceiraExpressao, dominiosTerceiraQuestao, dadosResultados)

#4. MINIMIZACAO
def MainQuartaQuestao(algoritimo):
   quartaExpressao = Expressoes.quartaExpressao
   dominiosQuartaQuestao = [-5.12, 5.12]

   dadosResultados = []
   valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
   for i in range(R):
     algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

     resultadoMinimizacao = algoritimoAtual(dominiosQuartaQuestao, quartaExpressao, True)
    
     if resultadoMinimizacao[1] < valorMinResultadoOtimo:
       valorMinResultadoOtimo = resultadoMinimizacao[1]
       resultadoOtimoMinimiazacao = resultadoMinimizacao
      
     dadosResultados.append(resultadoMinimizacao)

   if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
     raise ValueError("Não foi possivel determinar o valor otimo.")


   ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
   print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
   Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, quartaExpressao, dominiosQuartaQuestao, dadosResultados)

#5. MINIMIZACAO
def MainQuintaQuestao(algoritimo):
   quintaExpressao = Expressoes.quintaExpressao
   dominiosQuintaQuestao = [ [-2,2], [-1,3]]

   dadosResultados = []
   valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
   for i in range(R):
     algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

     resultadoMinimizacao = algoritimoAtual(dominiosQuintaQuestao, quintaExpressao, True)
    
     if resultadoMinimizacao[1] < valorMinResultadoOtimo:
       valorMinResultadoOtimo = resultadoMinimizacao[1]
       resultadoOtimoMinimiazacao = resultadoMinimizacao
      
     dadosResultados.append(resultadoMinimizacao)

   if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
     raise ValueError("Não foi possivel determinar o valor otimo.")


   ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
   print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
   Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, quintaExpressao, dominiosQuintaQuestao, dadosResultados)

##6. MAXIMIZACAO
def MainSextaQuestao(algoritimo):
  sextaExpressao = Expressoes.sextaExpressao
  dominiosSextaQuestao = [[-1,3] , [-1,3]]
  dadosResulados = []
  valorMaxResultadotimo = VALOR_INVALIDO_MAXIMIZACAO
  
  for i in range(R):
    algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

    resultadoMaximizacao = algoritimoAtual(dominiosSextaQuestao, sextaExpressao, False)

    if resultadoMaximizacao[1] > valorMaxResultadotimo:
      valorMaxResultadotimo = resultadoMaximizacao[1]
      resultadoOtimoMaximizacao = resultadoMaximizacao
      
    dadosResulados.append(resultadoMaximizacao)


  if(valorMaxResultadotimo == VALOR_INVALIDO_MAXIMIZACAO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da Maximizacao" , resultadoOtimoMaximizacao)
  Graficos.imprimirGrafico(resultadoOtimoMaximizacao , sextaExpressao, dominiosSextaQuestao, dadosResulados)

#7. Minimização
def MainSetimaQuestao(algoritimo):
   setimaExpressao = Expressoes.setimaExpressao
   dominiosSetimaQuestao = [ [0,np.pi], [0,np.pi]]

   dadosResultados = []
   valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
   for i in range(R):
     algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

     resultadoMinimizacao = algoritimoAtual(dominiosSetimaQuestao, setimaExpressao, True)
    
     if resultadoMinimizacao[1] < valorMinResultadoOtimo:
       valorMinResultadoOtimo = resultadoMinimizacao[1]
       resultadoOtimoMinimiazacao = resultadoMinimizacao
      
     dadosResultados.append(resultadoMinimizacao)
     print(resultadoOtimoMinimiazacao)

   if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
     raise ValueError("Não foi possivel determinar o valor otimo.")


   for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
   print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)

   Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, setimaExpressao, dominiosSetimaQuestao, dadosResultados)

#8. Minimização
def MainOitavaQuestao(algoritimo):
   oitavaExpressao = Expressoes.oitavaExpressao
   dominionsOitavaQuestao = [ [-200,20], [-200,20]]

   dadosResultados = []
   valorMinResultadoOtimo = VALOR_INVALIDO_MINIMIZACAO
  
   for i in range(R):
     algoritimoAtual = rodarAlgoritimoDeBusca(Algoritmos.ALGORITIMOS_IMPLEMENTADOS[algoritimo])

     resultadoMinimizacao = algoritimoAtual(dominionsOitavaQuestao, oitavaExpressao, True)
    
     if resultadoMinimizacao[1] < valorMinResultadoOtimo:
       valorMinResultadoOtimo = resultadoMinimizacao[1]
       resultadoOtimoMinimiazacao = resultadoMinimizacao
      
     dadosResultados.append(resultadoMinimizacao)
     print(resultadoOtimoMinimiazacao)

   if(valorMinResultadoOtimo == VALOR_INVALIDO_MINIMIZACAO):
     raise ValueError("Não foi possivel determinar o valor otimo.")


   for resultado in dadosResultados: print("RESULTADOS DA RODADA: -> ", resultado)
   print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)

   Graficos.imprimirGrafico(resultadoOtimoMinimiazacao, oitavaExpressao, dominionsOitavaQuestao, dadosResultados)

print('Trabalho de AV3')

RODAR_QUESTAO = {
  1 : MainPrimeiraQuestao,
  2 : MainSegundaQuestao,
  3 : MainTerceiraQuestao,
  4 : MainQuartaQuestao,
  5 : MainQuintaQuestao,
  6 : MainSextaQuestao,
  7 : MainSetimaQuestao, #-> Funcao estranha
  8 : MainOitavaQuestao 
}

RODAR_QUESTAO[8]('hillClimbing')