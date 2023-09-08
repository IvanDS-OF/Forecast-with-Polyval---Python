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





## Simulación / Simulation






