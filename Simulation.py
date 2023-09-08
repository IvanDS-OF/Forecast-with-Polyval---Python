# Código para hacer un pron+ostico de el comportamiento de un sistema
# Created by Eng. Ivan Duran


# First import all the libraries
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import time

def fx(x1,coef): 
    """
    Función para hacer calculo de predicción
    """
    fx=0
    n = len(coef) - 1
    for p in coef:
        fx = fx+p*x1**n
        n = n-1
    return fx


ceroDer = []
guardar=[]

V = [0.0 for i in range (0, 21)]

vec_datos = [0.0 for i in range (0, 21)]


x = np.arange(0,101,1)
es = np.arange(0,20,1)


fig1, axs1 = plt.subplots()


for j in range(0,200):
    axs1.axis([j, j+25, -1.5, 1.5]) #ylim(xmin, xmax, ymin, ymax)
    
    grado = 5
    tiempo = np.arange(j, j+21, 1) #Generamos un vector para realizar los sampleos con recpecto del tiempo
    #print(tiempo)

    
    #np.polifit (x, y, grado)
    coef0 = np.polyfit(np.array(tiempo), np.array(vec_datos[j:j+21]), grado)
    coef1 = np.polyfit(np.array(tiempo), np.array(vec_datos[j:j+21]), 2)
    #print(coef)
    #print(np.size(coef))
    #np.polyvail(coef, x) x = datos de más
    #p = np.polyval(coef, 102)
    #print(p)
    #print(np.size(p))

    for v in np.arange(j+20,j+25, 0.5):
        p = np.polyval(coef1,v)
        V.append(p)

    print("El valor de V es: ", len(V))

    #tiempo1 = np.linspace(0,20,200) #Eje X especial para hacer la predicción
    incremento = 0.5
    tiempo1 = np.arange(j,j+21, incremento)
    nPrueba0 = fx(tiempo1, coef0)   #funcion


    #Los valores a derivar son nPruebas
    #print("datos de predicción")
    #print(nPrueba)
    #print(np.size(nPrueba))

    fun0 = nPrueba0
    
    t = incremento

    #print("derivada")
    #print(der)
    #plt.close()
    #print(V)
    #print(len(V[20:]))
    ss = np.arange(j+20, j+25, 0.49)
    print("El valor de SS es: ", len(ss))
    
    axs1.set_title("Prueba POT")
    axs1.plot(tiempo, vec_datos[j:j+21], c="b", linewidth="2", label='MEDICION')
    #plt.plot(np.arange(101,107,1), coef, c="r")
    axs1.grid()
    plt.legend(loc='upper left', fontsize=8)
    axs1.scatter(ss, V[20:], c = "r")

         
    #plt.show()
    #plt.pause(2)
    plt.pause(1)
    num = float(input())
    vec_datos.append(num)

    V = [0.0 for i in range (0, 21)]
    print("El len de VVV es: ",  len(V))
    axs1.cla()





