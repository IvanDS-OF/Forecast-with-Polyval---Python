# Forecast-with-Polyfit---Python
This code pretends to obtain a simple forecast with Polyval function - PYTHON
Este es un código que pretende obtener un pronóstico simple usando la función Polyval en Python. 

## Pronóstico / Forecast
El pronóstico es una previsión de eventos futuros del comportamiento de un sistema en base a datos pasados comprobables registrados. Podemos encontrar un ejemplo sencillo de el pron+ostico en las noticias a la hora de las presentaciones del clima, en donde se presenta un pronóstico del tiempo. 


## Polyfit
Polyfit es una función de ls librería de **numpy** y la podemos mandar a llamar de la siguuiente manera: 

```
import numyp as np
np.polyval(x, y, grado)
```
Los argumentos que son obligatorios introducir son:

x == array : Representa los valores en el eje de las X, en caso de ser aplicado a una serie temporal podemos poner al vector de tiempo.
y == array : Representa los valores del eje de las y's, en caso de ser aplicado a una serie temporan podemos poner al vecor de la información
grado == int 

Recordemos brvemente la ecuación de la función polyval, lo que la función hace es minimizar el error cuadrado mediante la siguiente ecuación:


$$ E = \sum_{j=0}^k [p (x_j) - y]^2 $$

De igual forma podemos encontrar más información [en el siguiente link](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html) que pertenece a la documentación oficial de la librería. 


## Código / Code
El código genera un pronóstico usando la función polyval, al mismo tiempo que la base de datos es posible que el usuario la llene en tiempo real introduciendo valores desde la terminal. 

Primero es necesario importar las librerias necesarias para el funcionamiento del programa como son: 

```
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import time
```
Posteriormente creamos dos vectores vacios con valores flotantes usando la forma de _list cmoprehension_

Luego inicializamos la figura en donde vamos a plotear la figura e inicializamos tanto una variable que será iterada de forma infinita y un ciclo **while True**.

Dentro del ciclo infinito podemos encontrar que primero vamos a fijar los ejes superiores e inferiores para mayor estabilidad la animación y al mismo tiempo colocamos una instrucción para que los ejes aterales se vayan actualzando cada que se agregue un nuevo valor a la lista.


## Simulación / Simulation






