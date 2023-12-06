import numpy as np
import matplotlib.pyplot as plt 
import Algoritmos


def imprimirGrafico(
        resultadoOtimoMaximizacao, 
        func, 
        dominio, 
        resultados,
        algoritimoUsado
    ):
    
    limiteSuperiorX1,limiteInferiorX1, limiteSuperiorX2, limiteInferiorX2 = Algoritmos.getLimites(dominio)

    # Criação do gráfico da função
    x1_vals = np.linspace(limiteInferiorX1, limiteSuperiorX1, 100)
    x2_vals = np.linspace(limiteInferiorX2, limiteSuperiorX2, 100)
    
    X1, X2 = np.meshgrid(x1_vals, x2_vals)

    Y = func(X1, X2)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X1, X2, Y, rstride=10, cstride=10, alpha=0.6, cmap='viridis')


    for resultado in resultados:
        # Plotar picos
        ax.scatter(resultado[0][0], resultado[0][1], resultado[1], marker='x', s=20, linewidth=3, color='blue')


    # Plota o ótimo global de forma mais destacada
    ax.scatter(resultadoOtimoMaximizacao[0][0], resultadoOtimoMaximizacao[0][1], resultadoOtimoMaximizacao[1], marker='x', s=200, linewidth=3, color='red', label='Ótimo Global')

    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1, x2)')
    ax.set_title('f(x1, x2)- '+  algoritimoUsado +'- Ponto Ótimo Global')
    ax.legend()

    plt.tight_layout()
    plt.show()


