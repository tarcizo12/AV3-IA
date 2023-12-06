import numpy as np
import matplotlib.pyplot as plt 
import Algoritmos


def imprimirGraficoDominioSimples(resultadoOtimoMinimiazacao, func, dominio):
    limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = Algoritmos.getLimites(dominio)

    # Criação do gráfico resultado minimizacao
    x1 = np.linspace(limiteInferiorX1, limiteSuperiorX2, 100)
    X1, X2 = np.meshgrid(x1, x1)
    Y = func(X1, X2)


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='jet')

    ax.scatter(resultadoOtimoMinimiazacao[0][0], resultadoOtimoMinimiazacao[0][1], resultadoOtimoMinimiazacao[1], marker='x', s=90, linewidth=3, color='red', label='Ótimo Global')

    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title('f(x1, x2) - Hill Climbing (Mínimo)')
    ax.legend()

    plt.tight_layout()
    plt.show()



def imprimirGraficoDominioComposto(resultadoOtimoMaximizacao, func, dominio):
    
    limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = Algoritmos.getLimites(dominio)

    # Criação do gráfico da função
    x1_vals = np.linspace(limiteInferiorX1, limiteSuperiorX1, 100)
    x2_vals = np.linspace(limiteInferiorX2, limiteSuperiorX2, 100)
    
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    Y = func(X1, X2)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='viridis')

    # Plota o ótimo global de forma mais destacada
    ax.scatter(resultadoOtimoMaximizacao[0][0], resultadoOtimoMaximizacao[0][1], resultadoOtimoMaximizacao[1], marker='x', s=200, linewidth=3, color='red', label='Ótimo Global')

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1, x2)')
    ax.set_title('f(x1, x2) - Hill Climbing (Máximo) - Ponto Ótimo Global')
    ax.legend()

    plt.tight_layout()
    plt.show()


