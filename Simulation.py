# Código para hacer un pron+ostico de el comportamiento de un sistema
# Created by Eng. Ivan Duran


# First at all,  import all the libraries
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import time

# Then define all the functions, in the same script. 


# Creamos los vectores vacios que serán llenados después en las iteraciones.
V = [0.0 for i in range (0, 21)]
vec_datos = [0.0 for i in range (0, 21)]

# Creamos la figura donde plotearemos la gráfica
fig1, axs1 = plt.subplots()
j = 0

# Comenzamos con las iteraciones.
while True:
    axs1.axis([j, j+25, -1.5, 1.5]) #ylim(xmin, xmax, ymin, ymax)
    
    tiempo = np.arange(j, j+21, 1) #Generamos un vector para realizar los sampleos con recpecto del tiempo

    coef1 = np.polyfit(np.array(tiempo), np.array(vec_datos[j:j+21]), 1)

    for v in np.arange(j+20,j+25, 0.5):
        p = np.polyval(coef1,v)
        V.append(p)

    ss = [ i+1 for i in np.linspace(j+20, j+25, 11) ]

    axs1.set_title("Prueba POT")
    axs1.plot(tiempo, vec_datos[j:j+21], c="b", linewidth="2", label='MEDICION')
    axs1.scatter(ss, V[20:], c = "r")
    plt.legend(loc='upper left', fontsize=8)
    axs1.grid()
    plt.pause(0.1)

    num = float(input())
    vec_datos.append(num)

    V = [0.0 for i in range (0, 21)]

    axs1.cla()
    
    j = j + 1

