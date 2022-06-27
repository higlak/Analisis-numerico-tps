import numpy as np
import matplotlib.pyplot as plt
#from metodos_busqueda_raices_rovi import *

def imagen_por_funcion(x):
    return 0.001*x*(x-1000)**2 -25000

def graficar(puntos_dominio, puntos_imagen):
    #pip3 install matplotlib
    plt.grid()  
    plt.plot(puntos_dominio,puntos_imagen)
    plt.title('Funcion De Rentabilidad')
    plt.xlabel('Kilos de producto')
    plt.ylabel('Utilidad unitaria')
    plt.xlim(0,1200)
    #plt.ylim(-1,18)
    plt.show()

def main():
    puntos_dominio = np.linspace(0,1200,1000)
    puntos_imagen = []

    for punto in puntos_dominio:
        puntos_imagen.append(imagen_por_funcion(punto))
    
    graficar(puntos_dominio, puntos_imagen)

main()



        