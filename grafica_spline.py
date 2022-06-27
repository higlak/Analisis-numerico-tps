import numpy as np
import matplotlib.pyplot as plt
from pseudo_spline import *

def elegir_spline(vector_splines, x):
    for spline in vector_splines:
        if spline.esta_dentro_del_intervalo(x):
            return spline
    raise ValueError('Valor no esta dentro del dominio de las splines')

def imagen_de_puntos_por_spline(vector_splines, vector_puntos):
    imagen = []
    for x in vector_puntos:
        spline_elegida = elegir_spline(vector_splines, x)
        imagen.append(spline_elegida.evaluar_en(x))
    return imagen

def graficar_por_spline(vector_puntos_dominio, vector_puntos_imagen):
    plt.grid()
    plt.plot(vector_puntos_dominio,vector_puntos_imagen)
    plt.title('Mauasa Katai')
    plt.xlabel('Posicion')
    plt.ylabel('Culo')
    plt.xlim(1,30)
    plt.ylim(-1,15)
    plt.show()
    

def main():
    
    vector_nodos_1 = [1,2,5,6,7,8,10,13,17]
    vector_imagen_1 = [3,3.7,3.9,4.2,5.7,6.6,7.1,6.7,4.5]
    derivada_0_1 = 1
    derivada_n_1 = -2/3

    vector_nodos_2 = [17,20,23,24,25,27,27.7]
    vector_imagen_2 = [4.5,7,6.1,5.6,5.8,5.2,4.1]
    derivada_0_2 = 3
    derivada_n_2 = -4

    vector_nodos_3 = [27.7, 28, 29, 30]
    vector_imagen_3 = [4.1, 4.3, 4.1, 3]
    derivada_0_3 = 1/3
    derivada_n_3 = -3/2
    
    vector_splines_1 = crear_splines(vector_nodos_1, vector_imagen_1, derivada_0_1, derivada_n_1)
    vector_splines_2 = crear_splines(vector_nodos_2, vector_imagen_2, derivada_0_2, derivada_n_2)
    vector_splines_3 = crear_splines(vector_nodos_3, vector_imagen_3, derivada_0_3, derivada_n_3)
    

    plt.scatter(vector_nodos_1, vector_imagen_1)
    plt.scatter(vector_nodos_2, vector_imagen_2)
    plt.scatter(vector_nodos_3, vector_imagen_3)

    vector_splines_resultante = []
    [vector_splines_resultante.append(elem_1) for elem_1 in vector_splines_1]
    [vector_splines_resultante.append(elem_2) for elem_2 in vector_splines_2]
    [vector_splines_resultante.append(elem_3) for elem_3 in vector_splines_3]

    x = np.linspace(1,30,1000)
    f_x = imagen_de_puntos_por_spline(vector_splines_resultante, x)

    graficar_por_spline(x, f_x)

main()