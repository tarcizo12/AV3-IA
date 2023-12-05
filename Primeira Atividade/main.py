import Algoritmos
import Expressoes
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 


VALOR_INVALIDO = 9999999999999999

def plotarGraficoMinimizacaoHillClimbing(resultadoOtimoMinimiazacao):
    # Criação do gráfico resultado minimizacao
    x1 = np.linspace(-100, 100, 1000)
    X1, X2 = np.meshgrid(x1, x1)
    Y = Expressoes.expressaoPrimeiraQuestao(X1, X2)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')

    #for resultado_otimo in resultados_otimos_globais:
    #    ax.scatter(resultado_otimo[0], resultado_otimo[1], resultado_otimo[2], marker='x', s=90, linewidth=3, color='green')

    # Destaca o resultado ótimo global com uma cor diferente
    ax.scatter(resultadoOtimoMinimiazacao[0][0], resultadoOtimoMinimiazacao[0][1], resultadoOtimoMinimiazacao[1], marker='x', s=90, linewidth=3, color='red', label='Ótimo Global')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x1, x2) - Hill Climbing')
    ax.legend()

    plt.tight_layout()
    plt.show()

def Main():
  print('Trabalho de AV3')
  R = 100

  primeiraExpressao = Expressoes.expressaoPrimeiraQuestao

  dominioPrimeiraQuestao = [-100, 100]
  dadosResultadosMinimizacaoHillClimbing = []
  valorMinresultadoOtimoMinimiazacao = VALOR_INVALIDO
  resultadoOtimoMinimiazacao = -1

  
  for i in range(R):
    resultado = Algoritmos.hillClimbing(dominioPrimeiraQuestao, primeiraExpressao)
    
    if resultado[1] < valorMinresultadoOtimoMinimiazacao:
      valorMinresultadoOtimoMinimiazacao = resultado[1]
      resultadoOtimoMinimiazacao = resultado
      
    dadosResultadosMinimizacaoHillClimbing.append(resultado)

  if(resultadoOtimoMinimiazacao == VALOR_INVALIDO):
    raise ValueError("Não foi possivel determinar o valor otimo.")


  ##for resultado in dadosResultadosMinimizacaoHillClimbing: print("RESULTADOS DA RODADA: -> ", resultado)
  print("Resultado Otimo da minimização" , resultadoOtimoMinimiazacao)
  plotarGraficoMinimizacaoHillClimbing(resultadoOtimoMinimiazacao)

Main()  